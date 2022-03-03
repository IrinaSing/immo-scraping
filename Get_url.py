""" 

What's the intent of this code?: 

The intent is to go to a webpage (here https://www.immoweb.be) and and get all the href/web links of different property listings.
This to then use these links individually and extract the needed property information.

How does it work?:

First we input the webpage link that shows all the properties for sale. We then create a loop that inserts a pagenumber in the link,
and goes towards the webpage. Once on the page it looks into the source code for the seperate property links, and puts these in a .txt file.
After it has gone through the required pages it closes the webdriver and page.
"""


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

for page in range(261,300):
    url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page='+ str(page)+ '&orderBy=relevance'

    driver.get(url)
    
    assert "Immoweb" in driver.title

    for elem in driver.find_elements_by_xpath("//a[@class='card__title-link']"):
        with open ("url_links.txt","a") as new:
            new.write(elem.get_attribute("href") + "\n")
            time.sleep(random.uniform(1.0, 2.0))
        #link_list.append(elem.get_attribute("href"))
    
assert "No results found." not in driver.page_source
driver.close()
