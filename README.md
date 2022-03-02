# IMMO scraping

## Description of the program

Our program can be used for scrapping real estate websites. It saves information about property for sale into CSV file. Here are the steps:

1. The program sends request to the page with houses and apartments for sale.
2. It collects links to the pages with detailed information about properties into a separate file.
3. Iterating through the links, the program collects data related to each property such as: location, price, number of bedrooms etc.
4. Collecting information in data frames.
5. Creating CSV file with database.

In our example we gather data from Belgian resource ImmoWeb, but the program can be adapted for scrapping from other resources.

## Installation

The program is based on Python, so be sure you have it installed on your computer.

This the list of the things you need to use the software and how to install them.

1. Clone the repo to your computer.
2. Install Requests  
   `$ pip3 install requests`

3. Install Beautiful Soup  
   `$ pip3 install beautifulsoup4`

4. Install Pandas  
   `$ pip3 install pandas`

## Usage
