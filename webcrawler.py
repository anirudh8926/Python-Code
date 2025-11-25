import re
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

def crawl(l: str) -> list:
    x = urllib.request.urlopen(l).read()
    y = BeautifulSoup(x, "lxml")
    z = y("a")
    q = list()
    for i in z:
        q.append(i.get("href", None))   # the stuff received from the beautifulsoup object is a list of key/value pairs.

    wikipedialinks = list()
    for i in q:
        if re.match(r"^https:\/\/\S+\.wikipedia\.org\/wiki\/", i):
            wikipedialinks.append(i)
            q.remove(i)
        else:
            pass
    return (wikipedialinks)

def crawlloop(arr):
    for i in arr:
        crawl(i)
        print(crawl(i))

m = crawl("https://en.wikipedia.org/wiki/Main_Page")
crawlloop(m)
