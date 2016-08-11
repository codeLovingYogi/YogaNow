#!/usr/bin/env python3
import re
import urllib.parse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

browser = webdriver.PhantomJS()
#browser.get('http://www.stantonstreetyoga.com/classes/schedule/')
browser.get('http://www.jivamuktiyoga.nyc/schedule/')

# wait for page to load schedule data
wait = WebDriverWait(browser, 20)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".healcode")))
# set the window size for screenshot
browser.set_window_size(1024, 768) 
browser.save_screenshot('schedule.png')

# parse html
soup = BeautifulSoup(browser.page_source, "html.parser")
# get scheduling data
schedule = soup.find('div', {'class': 'schedule'})
#print(schedule.prettify())

# get list of classes
results = []

# find classes based on mbo schedule data organized in odd/even rows
yoga_classes = soup.find_all('tr', {'class': 'odd'})
yoga_classes2 = soup.find_all('tr', {'class': 'even'})

# get information about each class
results = []
for i in range(len(yoga_classes)):
	start_time = yoga_classes[i].find('span', {'class': 'hc_starttime'}).get_text()
	results.append({'start': start_time})
	
	end_time = yoga_classes[i].find('span', {'class': 'hc_endtime'}).get_text()
	results[i]['end'] = end_time
	
	description = yoga_classes[i].find('span', {'class': 'classname'}).get_text()
	results[i]['description'] = description
	
	teacher = yoga_classes[i].find('span', {'class': 'trainer'}).get_text()
	results[i]['teacher'] = teacher
	
print('num results: ', len(results))

for j in range(len(results)):
	for key, value in results[j].items():
		print(key, ': ', value)	