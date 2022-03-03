"""
What is the intent of this code?: 

After we have gathered the property links and checked for duplicates (see Data folder Readme.md) we want to go over each of these links and extract the needed information.

How does this code work?:

We first enter our Data folder for the filtered.url links and loop over each of them (or a range of them). We also define several lists, each with a specific bit of information
about the property. Once on the webpage we take the content using Beautiful Soup and put it in a variable called soup. This soup variable is then put in a Json object, and every
required bit of information is appended in beforementioned lists.

All of these lists are then put into a dataframe using pandas, which is then extracted into a csv file. This way we have a structured .csv file with all the attributes of our
properties.

"""




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

path = "./Data/filtered_url.txt"

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

    """
    Looping over the property links
    """
    for each in lines[0:100]:
        url = each
        r = requests.get(url)
        # print(url, r.status_code)
        soup = BeautifulSoup(r.content, "lxml")
        
        """ 
        Taking the content in soup and extracting the scripts with needed information.
        """
        
        homeinfo=''
        for elem in soup.find_all("script"):
            if 'window.dataLayer' in elem.text:
                homeinfo+=elem.text
                
        homeinfo=homeinfo[34::]
        homeinfo=homeinfo.replace('\n','')
        homeinfo=homeinfo.replace('];','')
        homeinfo=homeinfo.replace("window.dataLayer","")

        """
        Creating a Json object and appending in the lists.
        """

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
        
        """
        Putting it all in dataframes.
        """
        
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
        
        
        """
        Putting it all in a .csv.
        """
        
        df.to_csv("Onehome.csv")

        

    
