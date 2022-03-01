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

for each in link_list:
    link = each
    r = requests.get(link)
    print(link, r.status_code)
    soup = BeautifulSoup(r.content, "lxml")
    soup.find_all("script")[1]
    time.sleep(1)
print(soup)