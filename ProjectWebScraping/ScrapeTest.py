from urllib.request import urlopen
from bs4 import BeautifulSoup

import urllib.error

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    if html is None:
        print("URL is not found")
    else:
        bsObj = BeautifulSoup(html.read(), features="html.parser");
        print(bsObj.h1)
except urllib.error.HTTPError as e:
    print(e)
else:
    pass
