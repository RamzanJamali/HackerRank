import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

file = open('chall_7.txt')
ciphertext = base64.b64decode(file.read())
key = b'YELLOW SUBMARINE'
backend = default_backend()

def decrypt_aes_128_ecb(ctxt, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data =  decryptor.update(ctxt) + decryptor.finalize()
    message = decrypted_data
    return message
print(decrypt_aes_128_ecb(ciphertext, key).decode())
