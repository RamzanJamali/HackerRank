import base64
import os
import random
from random import randint
from math import ceil
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()


def pkcs7_pad(message, block_size):
    padding_length = block_size - ( len(message) % block_size )
    if padding_length == 0:
        padding_length = block_size
    padding = bytes([padding_length]) * padding_length
    return message + padding

def pkcs7_strip(data):
    padding_length = data[-1]
    return data[:- padding_length]


def split_bytes_in_blocks(x, blocksize):
    nb_blocks = ceil(len(x)/blocksize)
    return [x[blocksize*i:blocksize*(i+1)] for i in range(nb_blocks)]

def bxor(a, b):
    "bitwise XOR of bytestrings"
    return bytes([ x^y for (x,y) in zip(a, b)])

def encrypt_aes_128_ecb(data, key):
    padded_data = pkcs7_pad(data, block_size=16)
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend = backend)
    encryptor = cipher.encryptor()
    return encryptor.update(padded_data)+ encryptor.finalize()

def decrypt_aes_128_ecb(ctxt, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend = backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ctxt) + decryptor.finalize()
    message = pkcs7_strip(decrypted_data)
    return message

def encrypt_aes_128_block(msg, key):
    '''unpadded AES block encryption'''
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(msg) + encryptor.finalize()


def encrypt_aes_128_cbc(msg, iv, key):
    result = b''
    previous_ctxt_block = iv
    padded_ptxt = pkcs7_pad(msg, block_size=16)
    blocks = split_bytes_in_blocks(padded_ptxt, blocksize=16)
    
    for block in blocks:
        to_encrypt = bxor(block, previous_ctxt_block)
        new_ctxt_block = encrypt_aes_128_block(to_encrypt, key)
        result += new_ctxt_block
        previous_ctxt_block = new_ctxt_block
    
    return result


def encryption_oracle(message, mode = None):
    global key
    global to_encrypt
    key = os.urandom(16)
    rand_header = os.urandom(randint(5,10))
    rand_footer = os.urandom(randint(5,10))
    to_encrypt = rand_header + message + rand_footer

    if mode == None:
        mode = random.choice(['ECB', 'CBC'])
    if mode == 'ECB':
        return encrypt_aes_128_ecb(to_encrypt, key)
    elif mode == 'CBC':
        iv = os.urandom(16)
        return encrypt_aes_128_cbc(to_encrypt, iv, key)


def test_ecb_128(ctxt):
    mess = decrypt_aes_128_ecb(ctxt, key)
    if mess == to_encrypt:
        return True


for _ in range(10):
    mode = random.choice(['ECB', 'CBC'])
    message = b'Z'*50
    ctxt = encryption_oracle(message, mode)
    detected_mode = 'ECB' if test_ecb_128(ctxt) else 'CBC'
    print(detected_mode)
    assert detected_mode == mode
