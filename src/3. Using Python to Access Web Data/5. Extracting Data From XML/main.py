import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

url = "https://py4e-data.dr-chuck.net/comments_1831263.xml"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print("Retrieved", len(data), "characters")
tree = ET.fromstring(data)

counts = tree.findall(".//count")
result = sum(int(count.text) for count in counts)

print(result)
