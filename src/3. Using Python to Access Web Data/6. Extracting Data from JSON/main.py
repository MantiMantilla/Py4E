import urllib.request
import urllib.parse
import urllib.error
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = "https://py4e-data.dr-chuck.net/comments_42.json"
url = "https://py4e-data.dr-chuck.net/comments_1831264.json"

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

comments = json.loads(data)["comments"]

result = sum(cmt["count"] for cmt in comments)

print(result)
