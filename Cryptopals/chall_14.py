import base64
import random
from random import randint
from math import ceil
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()

def encrypt_aes_128_block(msg, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(msg) + encryptor.finalize()

def encrypt_aes_128_ecb(msg, key):
    block_size = 16
    padded_msg = pkcs7_pad(msg, block_size)
    return b''.join([
        encrypt_aes_128_block(block, key)
        for block in split_bytes_in_blocks(padded_msg, block_size)
    ])

def split_bytes_in_blocks(x, blocksize):
    nb_blocks = ceil(len(x)/blocksize)
    return [x[blocksize*i:blocksize*(i+1)] for i in range(nb_blocks)]

def pkcs7_pad(message, block_size):
    padding_length = block_size - ( len(message) % block_size )
    if padding_length == 0:
        padding_length = block_size
    padding = bytes([padding_length]) * padding_length
    return message + padding

class Oracle:
    def __init__(self):
        self.key = os.urandom(16)
        self.prefix = os.urandom(randint(1,15))
        self.target = base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg"
            "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq"
            "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg"
            "YnkK"
            )

    def encrypt(self,message):
        return encrypt_aes_128_ecb(self.prefix + message + self.target, self.key)

oracle = Oracle()
prev_length = len(oracle.encrypt(b''))

for i in range(20):
    length = len(oracle.encrypt(b'X'*i))
    if length != prev_length:
        block_size = length - prev_length
        size_prefix_plus_target_aligned = prev_length
        min_known_ptxt_size_to_align = i
        break
else:
    raise Exception('did not detect any change in ciphertext')

assert block_size == 16

prev_blocks = None

for i in range(1,block_size+1):
    blocks = split_bytes_in_blocks(oracle.encrypt(b'X'*i), block_size)
    if prev_blocks != None and blocks[0] == prev_blocks[0]:
        prefix_size = block_size - i + 1
        break
    prev_blocks = blocks
else:
    raise Exception('did not detect constant ciphertext blocks')

assert prefix_size == len(oracle.prefix)

target_size = size_prefix_plus_target_aligned - min_known_ptxt_size_to_align - prefix_size

assert target_size == len(oracle.target)

know_target_bytes = b""

for _ in range(target_size):
    r = prefix_size
    k = len(know_target_bytes)
    padding_length = (-k-1-r)% block_size
    padding = b"X" * padding_length

    target_block_number = (k+r)// block_size
    target_slice = slice(target_block_number*block_size, (target_block_number+1)*block_size)
    target_block = oracle.encrypt(padding)[target_slice]

    for i in range(2**8):
        message = padding + know_target_bytes + bytes([i])
        block = oracle.encrypt(message)[target_slice]
        if block == target_block:
            know_target_bytes += bytes([i])
            break

print(know_target_bytes.decode())
