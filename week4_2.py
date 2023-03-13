import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

init = 0

url = 'http://py4e-data.dr-chuck.net/known_by_Konstancja.html'
for i in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")


# Retrieve all of the anchor tags

    tags = soup('a')
    for tag in tags:
        new_url = tag.get('href', None)
        name = tag.contents[0]
        init = init + 1
        if init == 18:
            url = new_url
            init = 0
            break
else:
    print(name)
