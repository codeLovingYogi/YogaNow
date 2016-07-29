#!/usr/bin/env python3
import re
import urllib.parse

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

browser = webdriver.PhantomJS()
browser.get('http://www.stantonstreetyoga.com/classes/schedule/')
sleep(3)

# Parse html
soup = BeautifulSoup(browser.page_source, "html.parser")
# Get list of classes
classes = soup.find_all('div', {'class': 'mainSL'})

# Print out html for classes
print(classes[0].prettify())