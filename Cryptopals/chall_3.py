import codecs

b = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

def single_char_xor(input_bytes, char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])

    output = (output_bytes, char_value)

    print(output_bytes, char_value)
for i in range(256):
    single_char_xor(b,i)
print("done")

