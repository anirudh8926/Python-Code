import urllib.request
import json
import ssl
import urllib.parse

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urlini = "http://py4e-data.dr-chuck.net/opengeo"
args = dict()
data = "Universitas Gadjah Mada"
args["q"] = data.strip()

url = urlini + "?" + urllib.parse.urlencode(args)
response = urllib.request.urlopen(url, context =ctx).read()
jsondata = json.loads(response)
print(jsondata)