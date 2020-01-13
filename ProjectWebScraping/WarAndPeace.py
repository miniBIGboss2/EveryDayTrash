from urllib.request import urlopen
from bs4 import BeautifulSoup
'''Находит все имена в книге'''
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
# находит все имена с тегом 'span' и атрибутом 'green'
# Имяна с зеленым шрифтом
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
