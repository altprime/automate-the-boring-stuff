'''
parsing with bs4

'''

import requests, bs4
reqs = requests.get("http://nostarch.com')
reqs.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(reqs.text)

exFile = open('example.html')
exSoup = bs4.BeautifulSoup(exFile)

# finding an element with the select() method
exSoup = bs4.BeautifulSoup(exFile.read())
elements_ = exSoup.select("#author")
type(elements_) # should return a list of len(elements_) = 1
elements_[0].getText() # returns author name
elements_[0].attrs # returns attributes {'id':'author'}

