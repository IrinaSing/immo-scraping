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
import urllib
import re
from tabulate import tabulate
import os

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

path = "filtered_url.txt"
price =[]

with open(path, "r") as fp:
    lines = fp.readlines()
    for each in lines[0:1]:
        url = each
        r = requests.get(url)
        print(url, r.status_code)
        soup = BeautifulSoup(r.content, "lxml")
        
        for elem in soup.find_all("p", attrs={"class": "classified__price"}):
            for each in elem.find_all("span", attrs={"class": "sr-only"}):
                price+=each.text
                print(each.text) 
       
#        data = json.loads(soup.find('script').string)
#        print (data)

    