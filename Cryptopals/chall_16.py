import base64
import random
from random import randint
from math import ceil
import os
import urllib
from itertools import zip_longest
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()


def bxor(a, b, longest=True):
    if longest:
        return bytes([ x^y for (x, y) in zip_longest(a, b, fillvalue=0)])
    else:
        return bytes([ x^y for (x, y) in zip(a, b)])

def split_bytes_in_blocks(x, blocksize):
    nb_blocks = ceil(len(x)/blocksize)
    return [x[blocksize*i:blocksize*(i+1)] for i in range(nb_blocks)]
    
def encrypt_aes_128_block(msg, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(msg) + encryptor.finalize()

def decrypt_aes_128_block(ctxt, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data =  decryptor.update(ctxt) + decryptor.finalize()
    return decrypted_data

class PaddingError(Exception):
    pass

def pkcs7_padding(message, block_size):
    padding_length = block_size - ( len(message) % block_size )
    if padding_length == 0:
        padding_length = block_size
    padding = bytes([padding_length]) * padding_length
    return message + padding

def pkcs7_strip(x, block_size):
    if not len(x) % block_size == 0:
        raise PaddingError
        
    last_byte = x[-1]
    
    # the 'int' is superfluous here
    # as last_byte is already an int (for Python a byte string is a list of integers)
    # but this way it's clearer what we are doing
    padding_size = int(last_byte)

    if padding_size > block_size:
        raise PaddingError('illegal last byte (greater than block size)')
    if padding_size == 0:
        raise PaddingError('illegal last byte (zero)')
    
    if not x.endswith(bytes([last_byte])*padding_size):
        raise PaddingError

    return x[:-padding_size]


def encrypt_aes_128_cbc(msg, iv, key):
    block_size = 16
    padded_msg = pkcs7_padding(msg, block_size)
    result = b''
    mask = iv
    for block in split_bytes_in_blocks(padded_msg, block_size):
        tmp = bxor(block, mask)
        enc_block = encrypt_aes_128_block(tmp, key)
        # in CBC, each block of ciphertext
        # is used as a XOR mask on the next block of plaintext
        mask = enc_block
        result += enc_block
    return result


def decrypt_aes_128_cbc(ctxt, iv, key):
    block_size = 16
    padded_msg = b''
    mask = iv
    for enc_block in split_bytes_in_blocks(ctxt, block_size):
        tmp = decrypt_aes_128_block(enc_block, key)
        padded_msg += bxor(mask, tmp)
        mask = enc_block
    return pkcs7_strip(padded_msg, block_size)


class Oracle:
    def __init__(self):
        self.key = os.urandom(16)

    def encrypt(self,msg):
        quoted_msg = urllib.parse.quote_from_bytes(msg).encode()

        full_msg = (b"comment1=cooking%20MCs;userdata=" + quoted_msg + b";comment2=%20like%20a%20pound%20of%20bacon")
        iv = os.urandom(16)
        ciphertext = encrypt_aes_128_cbc(full_msg, iv, self.key)

        return {"iv":iv, "ciphertext":ciphertext}

    def decrypt_and_check_admin(self,ctxt):
        ptxt = decrypt_aes_128_cbc(ctxt["ciphertext"],ctxt["iv"], self.key)

        if b";admin=true;" in ptxt:
            return True
        else:
            return False


oracle = Oracle()

pad = bxor(b";admin=true", b"X"*11)
cryptogram = oracle.encrypt(b"X"*11)

cryptogram["ciphertext"] = bxor(cryptogram["ciphertext"], b'\x00'*16 + pad)
print("decrypted:", decrypt_aes_128_cbc(cryptogram["ciphertext"], cryptogram["iv"], oracle.key))

print("admin:", oracle.decrypt_and_check_admin(cryptogram))
