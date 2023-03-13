def repeat_key_xor(message_bytes, key):
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes


message = b"""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = b'ICE'

ciphertext = repeat_key_xor(message, key)
print(ciphertext.hex())
