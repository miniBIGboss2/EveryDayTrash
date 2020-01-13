from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html.read(), features="html.parser")
        title = bs_obj.body.h1
    except AttributeError as e:
        print(e)
        return None
    return title


Title = get_title("https://starcitygames.com/ultimate-guard-flipntray-mat-case-black/")
if Title is None:
    print("title could not be found")
else:
    print(Title)

# https://starcitygames.com/
# http://www.pythonscraping.com/pages/page1.html
