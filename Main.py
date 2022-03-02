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


with open(path, "r") as fp:
    lines = fp.readlines()
    for each in lines[100:105]:
        url = each
        r = requests.get(url)
        print(url, r.status_code)
        soup = BeautifulSoup(r.content, "lxml")

        homeinfo=''
        for elem in soup.find_all("script"):
            if 'window.dataLayer' in elem.text:
                homeinfo+=elem.text

        homeinfo=homeinfo[34::]
        homeinfo=homeinfo.replace('\n','')
        homeinfo=homeinfo.replace('];','')
        homeinfo=homeinfo.replace("window.dataLayer","")
        
        js_obj = json.loads(homeinfo)
        print(js_obj["classified"]["type"])
        print(js_obj["classified"]["price"])
        print(js_obj["classified"]["zip"])
        print(js_obj["classified"]["transactionType"])
        print(js_obj["classified"]["kitchen"]["type"])
        print(js_obj["classified"]["energy"]["heatingType"])
        print(js_obj["classified"]["subtype"])
        print(js_obj["classified"]["land"]["surface"])

        print(js_obj["classified"]["bedroom"]["count"])

    """with open(path, "r") as fp:
    lines = fp.readlines()
    for each in lines[100:105]:
        url = each
        r = requests.get(url)
        print(url, r.status_code)
        soup = BeautifulSoup(r.content, "lxml")
 
        info=''

        for elem in soup.find_all("script"):
            if "window.dataLayer" in elem.text:
                info+=elem.text
            
        info=info[34::]
        info=info.replace('\n','')
        info=info.replace('];','')
        info=info.replace("window.dataLayer","")


        js_obj = json.loads(info)
        print(js_obj["classified"]["type"])
        print(js_obj["classified"]["price"])
        print(js_obj["classified"]["zip"])
        print(js_obj["classified"]["transactionType"])
        print(js_obj["classified"]["kitchen"]["type"])
        print(js_obj["classified"]["energy"]["heatingType"])
        print(js_obj["classified"]["subtype"])
        print(js_obj["classified"]["land"]["surface"])

        print(js_obj["classified"]["bedroom"]["count"])


        print(js_obj["classified"]["outdoor"]["terrace"]["exists"])
        print(js_obj["classified"]["outdoor"]["garden"]["surface"])
        print(js_obj["classified"]["wellnessEquipment"]["hasSwimmingPool"])
        print(js_obj["classified"]["condition"]["isNewlyBuilt"])
        print(js_obj)"""
        
        
        
        
        
        
        
    """for elem in soup.find_all("div", attrs={"class": "classified__information--address"}):
            for local in elem.find_all("span"):
                locality+=each.text
                print(local.text) 
            
        for elem in soup.find_all("div", attrs={"class": "classified__header-primary-info"}):
            for each in elem.find_all("h1", attrs={"class":"classified__title"}):
                property_type+=each
                print(each) 
      
        for elem in soup.find_all("p", attrs={"class": "classified__price"}):
            for each in elem.find_all("span", attrs={"class": "sr-only"}):
                price+=each.text
                print(each.text)"""

#        data = json.loads(soup.find('script').string)
#        print (data)

    