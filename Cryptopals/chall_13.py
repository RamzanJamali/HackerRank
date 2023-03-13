import base64
import os
import random
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()


def encrypt_aes_128_ecb(data, key):
    padded_data = pkcs7_padding(data, block_size=16)
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend = backend)
    encryptor = cipher.encryptor()
    return encryptor.update(padded_data)+ encryptor.finalize()


def decrypt_aes_128_ecb(ctxt, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend = backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ctxt) + decryptor.finalize()
    message = pkcs7_strip(decrypted_data)
    return message


def pkcs7_padding(message, block_size):
    padding_length = block_size - ( len(message) % block_size )
    if padding_length == 0:
        padding_length = block_size
    padding = bytes([padding_length]) * padding_length
    return message + padding


def pkcs7_strip(data):
    padding_length = data[-1]
    return data[:- padding_length]

def split_bytes_in_blocks(string, block_size):
    return (string[0+i:length+i] for i in range(0, len(string), block_size))

class Profile_Manager:
    def __init__(self):
        self.key = os.urandom(16)

    @staticmethod
    def parse(byte_string):
        string = byte_string.decode()
        result = dict(pair.split('=')
                      for pair in string.split('&'))
        return result

    @staticmethod
    def profile_for(email):
        if b"&" in email or b"=" in email:
            raise ValueError("Invalid Email Address")
        return b"email=" + email + b'&uid=10&role=user'

    def get_encrypted_profile(self, email):
        profile = self.profile_for(email)
        return encrypt_aes_128_ecb(profile, self.key)

    def decrypt_and_parse_profile(self, ctxt):
        profile = decrypt_aes_128_ecb(ctxt, self.key)
        return self.parse(profile)

manager = Profile_Manager()

assert( manager.profile_for(b"email@example.com") == b'email=email@example.com&uid=10&role=user')

assert( manager.parse(b'email=email@example.com&uid=10&role=user') == {'email': 'email@example.com', 'role': 'user', 'uid': '10'})

encrypted_profile = manager.get_encrypted_profile(b"email@example.com")

assert( manager.decrypt_and_parse_profile(encrypted_profile) == {'email': 'email@example.com', 'role': 'user', 'uid': '10'})


block_size = 16
target_email = b"aaaaaaaaaaaemail@attacker.com"
print("Using email address:", target_email)
print("blocks:", split_bytes_in_blocks(manager.profile_for(target_email), block_size))
ciphertext_1 = manager.get_encrypted_profile(target_email)


chosen_plaintext = pkcs7_padding(b"admin", block_size)
fabricated_email = b"nextBlockShouldSt@rt.Here:" + chosen_plaintext
print("Using fabricated email:", fabricated_email)
print("Blocks:", split_bytes_in_blocks(manager.profile_for(fabricated_email), block_size))


ciphertext_2 = manager.get_encrypted_profile(fabricated_email)
cut_block = ciphertext_2[2*block_size: 3*block_size]
new_ciphertext = ciphertext_1[:-block_size] + cut_block
profile = manager.decrypt_and_parse_profile(new_ciphertext)

print("Profile obtained:")
print(profile)

assert profile['role'] == 'admin'
