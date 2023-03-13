import codecs
import sys
import re

fhand = open("hidden_message.txt")

def single_char_xor(input_bytes, char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes, char_value

new_list = list()
for text in fhand:
    text = text.strip()
    new_list.append(text)

final_list = list()
for line in new_list:
    line = bytes.fromhex(line)
    for i in range(256):
        member = single_char_xor(line,i)
        text = member[0]
       
#       text = text.split()
        try:
            text = text.decode("utf-8")
            final_list.append(text)
        except:
            continue


print("done")

for lyn in final_list:
        x = re.findall('[a-zA-Z]+\S+[a-zA-Z]',lyn)
        if len(x) > 4:
            print(lyn)
