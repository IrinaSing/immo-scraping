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
homeinfo=''

with open(path, "r") as fp:
    lines = fp.readlines()
    for each in lines[0:3]:
        url = each
        r = requests.get(url)
        print(url, r.status_code)
        soup = BeautifulSoup(r.content, "lxml")
        info = soup.find_all("script")
        if 'window.dataLayer' in info:
            homeinfo+=info
            #print(elem.text)
            #convert string to  object
            print(homeinfo)
            """homeinfo=homeinfo[34::]
            homeinfo=homeinfo.replace('\n','')
            homeinfo=homeinfo.replace('];','')
            js_obj = json.loads(homeinfo)
            print(homeinfo)"""
