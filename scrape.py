#!/usr/bin/env python3
import re
import urllib.parse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

browser = webdriver.PhantomJS()
browser.get('http://www.stantonstreetyoga.com/classes/schedule/')

# wait for page to load schedule data
wait = WebDriverWait(browser, 20)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".healcode")))
# set the window size for screenshot
browser.set_window_size(1024, 768) 
browser.save_screenshot('schedule.png')

# parse html
soup = BeautifulSoup(browser.page_source, "html.parser")
# get scheduling data
schedule = soup.find('div', {'class': 'mainSL'})
#print(schedule.prettify())

# get list of classes
yoga_classes = soup.find_all('tr', {'class': 'odd'})

# get information about each class
for i in range(len(yoga_classes)):
	#print(classes[i].prettify())
	start_time = yoga_classes[i].find('span', {'class': 'hc_starttime'}).get_text()
	print('start: ', start_time)
	end_time = yoga_classes[i].find('span', {'class': 'hc_endtime'}).get_text()
	print('end: ', end_time)
	description = yoga_classes[i].find('span', {'class': 'classname'}).get_text()
	print('class: ', description)
	teacher = yoga_classes[i].find('span', {'class': 'trainer'}).get_text()
	print('teacher: ', teacher)