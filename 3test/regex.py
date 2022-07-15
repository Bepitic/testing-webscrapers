""" test3 getting a webpage """
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs_obj = BeautifulSoup(html)

images = bs_obj.find_all("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})

for image in images:
    print(image["src"])
