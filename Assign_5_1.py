import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum=0

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_546019.xml')

for line in fhand:
    line = line.decode()
    print(line)
    tree = ET.fromstring(line)
    counts = tree.findall('count')
    for item in counts:
        # Look at the parts of a tag
        num = item.find('count').text
        sum = sum + int(num)

print(sum)
