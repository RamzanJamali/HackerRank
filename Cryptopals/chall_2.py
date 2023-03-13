import codecs

def xor_byte_strings(input1, input2):
    return bytes([a ^ b for a, b in zip(input1, input2)])

hex1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
hex2 = bytes.fromhex("686974207468652062756c6c277320657965")

print(xor_byte_strings(hex1, hex2).hex())
