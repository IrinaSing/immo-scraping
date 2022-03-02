"""
In this file we try to connect to an immo webpage and loop over all it's pages
of properties for sale. In each page we go look for all the href links for each listing.
These are then stored in an text file. 

Afterwards we use Excel to remove the duplicates and create a seperate "filtered text
file with all the unique links to properties. This will be the start for our scraping.
"""

import time
import random

from selenium import webdriver


driver = webdriver.Edge()


for page in range(261,300):
    url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page='+ str(page)+ '&orderBy=relevance'

    driver.get(url)
    
    assert "Immoweb" in driver.title

    for elem in driver.find_elements_by_xpath("//a[@class='card__title-link']"):
        with open ("url_links.txt","a") as new:
            new.write(elem.get_attribute("href") + "\n")
            time.sleep(random.uniform(1.0, 2.0))

    
assert "No results found." not in driver.page_source
driver.close()
