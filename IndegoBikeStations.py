
#geolocator = GoogleV3()

# noinspection PyUnresolvedReferences
import requests

# noinspection PyUnresolvedReferences
from bs4 import BeautifulSoup

# noinspection PyUnresolvedReferences
from selenium import webdriver

import pandas as pd

import time

''' Python code to get the addresses of all Indego's bike stations in Philadelphia. '''

url = 'https://www.rideindego.com/suggest-a-station/'
driver = webdriver.Chrome(executable_path="path to your chrome driver..../chromedriver")
driver.get(url)
time.sleep(20)  # wait 20 seconds for the site to load.

html = driver.page_source
soup = BeautifulSoup(html, features='html.parser')

def getindegoStationsAddress():

    indegoStations = []

    for station in soup.findAll('div', attrs={'id': 'gfgeo-map-7_1'}):

        for station in soup.find('div', attrs={'style': 'position: absolute; left: 0px; top: 0px; z-index: 106; width: 100%;'}):

            indegoStations.append(station.get('title', 'no title attribute'))

        dictionary = {"Title": indegoStations}

        df = pd.DataFrame(dictionary)

    return df

results = getindegoStationsAddress()

''' Finally, output the results into your Documents folder. '''
results.to_excel('/Users/username/Documents/YOUR_FILE_NAME.xlsx')
