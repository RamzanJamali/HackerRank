import base64
import os
import random
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()


class ECB_Oracle:
    def __init__(self):
        self.key = os.urandom(16)

    def encrypt(self, msg):
        return encrypt_aes_128_ecb(msg + Data_To_Append, self.key)

def pkcs7_strip(data):
    padding_length = data[-1]
    return data[:- padding_length]

def encrypt_aes_128_ecb(data, key):
    padded_data = pkcs7_pad(data, block_size=16)
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend = backend)
    encryptor = cipher.encryptor()
    return encryptor.update(padded_data)+ encryptor.finalize()

def pkcs7_pad(message, block_size):
    padding_length = block_size - ( len(message) % block_size )
    if padding_length == 0:
        padding_length = block_size
    padding = bytes([padding_length]) * padding_length
    return message + padding

def test_ecb_128(ctxt):
    mess = decrypt_aes_128_ecb(ctxt, oracle.key)
    return mess

def decrypt_aes_128_ecb(ctxt, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend = backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ctxt) + decryptor.finalize()
    message = pkcs7_strip(decrypted_data)
    return message

Data_To_Append = base64.b64decode("""Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybG
                                  llcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK""")

def find_block_size(oracle):
    curr_ctxt = None
    for i in range(2,20):
        prev_ctxt = curr_ctxt or oracle.encrypt(b"A"*1)
        curr_ctxt = oracle.encrypt(b"A"*i)
        if prev_ctxt[:4] == curr_ctxt[:4]:
            return i-1

oracle = ECB_Oracle()
ctxt = oracle.encrypt(b'A'*50)
block_size = find_block_size(oracle)
assert block_size == 16

assert test_ecb_128(oracle.encrypt(b'A'*50))

def find_payload_length(oracle):
    prev_length = len(oracle.encrypt(b''))
    for i in range(20):
        length = len(oracle.encrypt(b'X'*i))
        if length != prev_length:
            return prev_length - i

def rec_one_more_byte_ecb(oracle, known_plaintext, block_size):
    k = len(known_plaintext)
    padd_len = (-k-1)% block_size
    padding = b"A" * padd_len
    target_block_number = len(known_plaintext)// block_size
    target_slice = slice(target_block_number * block_size, (target_block_number + 1) * block_size)
    target_block = oracle.encrypt(padding)[target_slice]

    for i in range(256):
        message = padding + known_plaintext + bytes([i])
        block = oracle.encrypt(message)[target_slice]
        if block == target_block:
            return bytes([i])


def rec_one_byte_at_time_ecb(oracle, block_size):
    known_plaintext = b""
    payload_len = find_payload_length(oracle)
    for _ in range(payload_len):
        new_known_byte = rec_one_more_byte_ecb(oracle, known_plaintext, block_size)
        known_plaintext = known_plaintext + new_known_byte

    return known_plaintext

secret = rec_one_byte_at_time_ecb(oracle, block_size)

print(secret.decode())
