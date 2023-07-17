# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Position of link to follow
# pos = 3
pos = 18

# Number of times to follow nested links
# rec = 4
rec = 7

# url = input("Enter - ")
# url = "https://py4e-data.dr-chuck.net/known_by_Fikret.html"
url = "https://py4e-data.dr-chuck.net/known_by_Mahek.html"

name = ""

for i in range(rec):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags
    tag = soup("a")[pos - 1]
    url = tag.get("href", None)
    name = tag.get_text()

print(name)
