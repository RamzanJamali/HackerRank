block_size = 16

class PaddingError(Exception):
    pass
def pkcs7_strip(x, block_size):
    if not len(x) % block_size == 0:
        raise PaddingError

    last_byte = x[-1]
    padding_size = int(last_byte)

    if not x.endswith(bytes([last_byte])*padding_size):
        raise PaddingError

    return x[:-padding_size]


assert pkcs7_strip(b'ICE ICE BABYS\x03\x03\x03', block_size) == b'ICE ICE BABYS'
print("Ok")
try:
    pkcs7_strip(b'ICE ICE BABY\x05\x05\x05\x05', block_size)
    pkcs7_strip(b'ICE ICE BABY\x01\x02\x03\x04', block_size)

except PaddingError:
    print("Error")

else:
    print("Error: Expected a padding error")
