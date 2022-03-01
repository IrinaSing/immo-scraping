import bs4
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import json
import re
import lxml.html
import time
import random
from random import randint
import logging
import collections
from time import gmtime, strftime

import re
from tabulate import tabulate
import os

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
link_list = []

for page in range(1,2):
    url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page='+ str(page)+ '&orderBy=relevance'

    driver.get(url)
    
    assert "Immoweb" in driver.title

    for elem in driver.find_elements_by_xpath("//a[@class='card__title-link']"):
        link_list.append(elem.get_attribute("href"))
    
assert "No results found." not in driver.page_source
driver.close()

locality =[]
    
for each in link_list:
    link = each
    r = requests.get(link)
    print(link, r.status_code)
    soup = BeautifulSoup(r.content, "lxml")
    soup.find_all("script")[1]
    time.sleep(1)
print(soup)

"""    for elem in soup.find_all("td", attrs={'class':'classified-table__data'}):
    #find_all("span", attrs={'class':'classified__information--address-row'}):
        #find_elements_by_xpath("//span[@class='classified__information--address-row']"):
        locality.append(elem.text)
        print(elem.text)"""

#print(len(locality))


"""
- Locality : <span class="classified__information--address-row">8420<span aria-hidden="true">—</span>De Haan<!----></span>
- Type of property (House/apartment): <h1 class="classified__title">Villafor sale</h1>
- Subtype of property (Bungalow, Chalet, Mansion, ...): 
- Price: <span class="sr-only">1650000€</span>
- Type of sale (Exclusion of life sales)
- Number of rooms: <p class="classified__information--property">
   4 bedrooms
   <span aria-hidden="true">|</span>
   499
   <span class="abbreviation"><span aria-hidden="true">
   m² </span> <span class="sr-only">
   square meters </span></span></p>
- Area
- Fully equipped kitchen (Yes/No)
- Furnished (Yes/No)
- Open fire (Yes/No)
- Terrace (Yes/No)
  - If yes: Area
- Garden (Yes/No)
  - If yes: Area
- Surface of the land
- Surface area of the plot of land
- Number of facades
- Swimming pool (Yes/No)
- State of the building (New, to be renovated, ...)
"""
