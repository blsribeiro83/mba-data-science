# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:54:05 2026

@author: Bruno
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://pythonscraping.com/pages/page1.html")
print (html.read())

html = urlopen("https://pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(),"html.parser")
print (bs.h1)