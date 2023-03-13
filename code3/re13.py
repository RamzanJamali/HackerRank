# Search for lines that start with From and a character
# followed by a two digit number between 00 and 99 followed by ':'
# Then print the number if it is greater than zero
import re

total = 0
hand = open('total.txt')
for line in hand:
    line = line.strip()
    x = re.findall('[0-9]+', line)
    if len(x)<1:continue
    for num in x:
        total = total + int(num)

print(total)
