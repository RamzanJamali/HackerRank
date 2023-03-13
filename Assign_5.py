import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
string = ''

address = 'http://py4e-data.dr-chuck.net/comments_546019.xml'


uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
string = data.decode()


tree = ET.fromstring(string)
print('User count: ', len(tree), tree)
counts = tree.findall('comments/comment/count')

for item in counts:
    num = item.text
    sum = sum + int(num)

print(sum)
