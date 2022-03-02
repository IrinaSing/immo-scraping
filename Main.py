import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

import re
# from tabulate import tabulate
import os

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

path = "filtered_url.txt"

with open(path, "r") as fp:
    lines = fp.readlines()
    type_property = []
    prices = []
    zip = []
    transactionType = []
    kitchen = []
    energy = []
    subtype = []
    land = []
    bedrooms = []
    terrace = []
    garden = []
    swimpool = []
    condition = []

    for each in lines[0:100]:
        url = each
        r = requests.get(url)
        # print(url, r.status_code)
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

        type_property.append(js_obj["classified"]["type"])
        prices.append(js_obj["classified"]["price"])
        zip.append(js_obj["classified"]["zip"])
        transactionType.append(js_obj["classified"]["transactionType"])
        kitchen.append(js_obj["classified"]["kitchen"]["type"])
        energy.append(js_obj["classified"]["energy"]["heatingType"])
        subtype.append(js_obj["classified"]["subtype"])
        land.append(js_obj["classified"]["land"]["surface"])

        bedrooms.append(js_obj["classified"]["bedroom"]["count"])


        terrace.append(js_obj["classified"]["outdoor"]["terrace"]["exists"])
        garden.append(js_obj["classified"]["outdoor"]["garden"]["surface"])
        swimpool.append(js_obj["classified"]["wellnessEquipment"]["hasSwimmingPool"])
        condition.append(js_obj["classified"]["condition"]["isNewlyBuilt"])
        
        #df = pd.DataFrame.from_dict(pd.json_normalize(js_obj), orient='columns')

        df = pd.DataFrame({"Type_property": type_property})
        df["Prices"] = prices
        df["zip"] = zip
        df["transactionType"] = transactionType
        df["kitchen"] = kitchen
        df["energy"] = energy
        df["subtype"] = subtype
        df["land"] = land
        df["bedrooms"] = bedrooms
        df["terrace"] = terrace
        df["garden"] = garden
        df["swimpool"] = swimpool
        df["condition"] = condition

        df.to_csv("Onehome.csv")

        

    