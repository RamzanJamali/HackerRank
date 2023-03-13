import urllib.request, urllib.parse, urllib.error
import json
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
count = 0
address = 'http://py4e-data.dr-chuck.net/comments_546020.json'


uh = urllib.request.urlopen(address, context=ctx)
data = uh.read().decode()
print('Retrieving', address)
info = json.loads(data)
print("Retrieved ", len(info), "\n")

for i in info["comments"]:
    num = i["count"]
    sum = sum + int(num)
    count = count +1

print(count)
print(sum)
