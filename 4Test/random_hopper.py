from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

'Retrieves a list of all Internal links found in a webpage'
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # finds all the links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

'Retrieves a list of all external links'
def getExternalLinks(bsObj, excludeUrl):
    internalLinks = []
    # finds all the links that begin with www or http and do not contain the current url
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def splitAddress(address):
    addressParts = address.replace("https://","").split("/")
    return addressParts

def getRandomExternalLink(staringPage):
    html = urlopen(staringPage)
    bsObj = BeautifulSoup(html)
    addr = splitAddress(staringPage)[0]
    externalLinks = getExternalLinks(bsObj, addr)
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj,addr)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startinSite):
    externalLink = getRandomExternalLink(startinSite)
    print("Link followed is: " + str(externalLink))
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
