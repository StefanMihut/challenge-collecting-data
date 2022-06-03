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
import concurrent.futures

driver = webdriver.Firefox()
link_list = []

for page in range(1,333):
    url = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page='+ str(page)

    driver.get(url)
    
    assert "Immoweb" in driver.title

    for elem in driver.find_elements_by_xpath("//a[@class='card__title-link']"):
        with open ("url_links.txt","a") as new:
            new.write(elem.get_attribute("href") + "\n")
            #time.sleep(random.uniform(1.0, 2.0))

assert "No results found." not in driver.page_source
driver.close()