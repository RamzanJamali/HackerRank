import base64
import os
import random
from math import ceil
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()

def bxor(a, b):
    "bitwise XOR of bytestrings"
    return bytes([ x^y for (x,y) in zip(a, b)])


def encrypt_aes_128_block(msg, key):
    '''unpadded AES block encryption'''
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(msg) + encryptor.finalize()


def decrypt_aes_128_block(ctxt, key):
    '''unpadded AES block decryption'''
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data =  decryptor.update(ctxt) + decryptor.finalize()
    return decrypted_data


def split_bytes_in_blocks(x, blocksize):
    nb_blocks = ceil(len(x)/blocksize)
    return [x[blocksize*i:blocksize*(i+1)] for i in range(nb_blocks)]

def pkcs7_padding(message, block_size):
    padding_length = block_size - ( len(message) % block_size )
    if padding_length == 0:
        padding_length = block_size
    padding = bytes([padding_length]) * padding_length
    return message + padding


def pkcs7_strip(data):
    padding_length = data[-1]
    return data[:- padding_length]


def encrypt_aes_128_cbc(msg, iv, key):
    result = b''
    previous_ctxt_block = iv
    padded_ptxt = pkcs7_padding(msg, block_size=16)
    blocks = split_bytes_in_blocks(padded_ptxt, blocksize=16)
    
    for block in blocks:
        to_encrypt = bxor(block, previous_ctxt_block)
        new_ctxt_block = encrypt_aes_128_block(to_encrypt, key)
        result += new_ctxt_block
        previous_ctxt_block = new_ctxt_block
    
    return result

def decrypt_aes_128_cbc(ctxt, iv, key):
    result = b''
    previous_ctxt_block = iv
    blocks = split_bytes_in_blocks(ctxt, blocksize=16)
    
    for block in blocks:
        to_xor = decrypt_aes_128_block(block, key)
        result += bxor(to_xor, previous_ctxt_block)
        assert len(result) != 0
        previous_ctxt_block = block
        
    return pkcs7_strip(result)


def main():
    iv = b'\x00' * algorithms.AES.block_size
    key = b'YELLOW SUBMARINE'

    fh = open('chall_10.txt')
    binary_data = base64.b64decode(fh.read())

    ctxt = encrypt_aes_128_cbc(binary_data, iv, key)
    plain = decrypt_aes_128_cbc(ctxt, iv, key)
    assert plain == binary_data
    print("Successfully executed!")


if __name__ == '__main__':
    main()
