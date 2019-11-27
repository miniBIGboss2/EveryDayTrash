from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_card_price():
    html = urlopen("https://starcitygames.com/liliana-of-the-veil-sgl-mtg-isd-105-enn/")
    bs_obj = BeautifulSoup(html, features="html.parser")
    card_price = bs_obj.find("span", {"class": "price price--withoutTax"})
    print(card_price.get_text())


def get_card_name():
    html = urlopen("https://starcitygames.com/liliana-of-the-veil-sgl-mtg-isd-105-enn/")
    bs_obj = BeautifulSoup(html, features="html.parser")
    card_name = bs_obj.find("dd", {"data-field": "Card Name"})
    print(card_name.get_text())


def get_card_image():
    html = urlopen("https://starcitygames.com/liliana-of-the-veil-sgl-mtg-isd-105-enn/")
    bs_obj = BeautifulSoup(html, features="html.parser")
    card_image = bs_obj.find("data-image-gallery-main data-zoom-image", {"class": "https://cdn11.bigcommerce.com/s-3b5vpig99v/images/stencil/1280x1280/products/204094/140256/LilianaOfTheVeil__29272.1569217185.jpg?c=2&imbypass=on"})
    print(card_image)


get_card_name()
get_card_image()
get_card_price()
