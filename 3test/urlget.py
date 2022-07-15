""" test3 getting a webpage """

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs_obj = BeautifulSoup(html)

for sibling in bs_obj.find("table", {"id":"giftList"}).tr:
    print(sibling)
