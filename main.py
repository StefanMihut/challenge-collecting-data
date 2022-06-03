from dataclasses import replace
from msilib.schema import tables
from multiprocessing import Value
from operator import index
from urllib.request import urlopen
import bs4
from h11 import Data
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
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from tabulate import tabulate
import os
import webbrowser
import urllib3
date = strftime("%Y-%m-%d")


driver = webdriver.Firefox()



def get_data_for_link(url):
    driver.get(url)
    table = driver.find_elements_by_xpath("//table/tbody/tr")

    data = {}

    for element in table:
        try:
            key = element.find_element_by_xpath(".//th").text
            value = element.find_element_by_xpath(".//td").text
            data[key]= value
        except:
            value=None

    return data

final_data =[]

with open("url_links.txt") as file:
    for url in file.readlines()[:10]:
        data=get_data_for_link(url)
        final_data.append(data)
        print(url)



df = pd.DataFrame(final_data)
df.to_csv("data.csv")
print(df)

#time.sleep(2)

driver.quit()


