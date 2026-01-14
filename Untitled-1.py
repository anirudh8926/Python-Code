import urllib.request
data = urllib.request.urlopen("https://www.py4e.com/code3/mbox.txt?PHPSESSID=9c53baa82978639cea66cb353a47b2c4").read()
for i in data:
    print(i)
    