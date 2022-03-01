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

driver.get("https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance")

assert "Immoweb" in driver.title

for listing in driver.find_elements_by_xpath("//article"):
    print("ok")
    
for elem in listing.find_elements_by_xpath("//a[@class='card__title-link']"):
    link_list.append(elem.get_attribute("href"))

print(link_list)

assert "No results found." not in driver.page_source
driver.close()