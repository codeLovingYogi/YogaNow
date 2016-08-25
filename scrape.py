#!/usr/bin/env python3
import re
import urllib.parse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

#link = 'http://www.stantonstreetyoga.com/classes/schedule/'
link = 'http://www.jivamuktiyoga.nyc/schedule/'


class YogaClassScraper(object):

    """Find yoga classes by scraping data from yoga studio schedules."""
    
    def __init__(self):
        self.browser = webdriver.PhantomJS()
        # set the window size for screenshot
        self.browser.set_window_size(1024, 768) 
    
    def find_classes(self):
        """Open page, feed HTML into BeautifulSoup, and find classes."""
        self.browser.get(link)
        # wait for page to load schedule data
        wait = WebDriverWait(self.browser, 20)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".healcode")))
        self.browser.save_screenshot('schedule.png')
        # store list of classes
        results = []
        # parse html
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        
        # get scheduling data
        #schedule = soup.find('div', {'class': 'schedule'})
        #print(schedule.prettify())
        
        # scrape list of classes based on mbo schedule data organized in odd/even rows
        yoga_classes = soup.find_all('tr', {'class': 'odd'})
        yoga_classes2 = soup.find_all('tr', {'class': 'even'})
        # scrape details about each class
        self.get_details(yoga_classes, results)
        self.get_details(yoga_classes2, results)

        return results

    def get_details(self, classlist, resultlist):
        """Get and store details about each yoga class."""
        for i in range(len(classlist)):
            start_time = classlist[i].find('span', {'class': 'hc_starttime'}).get_text().strip()
            time = classlist[i].find('span', {'class': 'hc_endtime'}).get_text().strip()
            end_time = re.search('[0-9]+.*', time).group(0)
            description = classlist[i].find('span', {'class': 'classname'}).get_text().strip()
            teacher = classlist[i].find('span', {'class': 'trainer'}).get_text().strip()
            resultlist.append({'start': start_time, 'end': end_time, 'description': description, 'teacher': teacher})

    def scrape(self):
        """Main method to start scraper and find yoga classes."""
        results = self.find_classes()
        print('num results: ', len(results))

        for j in range(len(results)):
            for key, value in results[j].items():
                print(key, ': ', value) 

        self.browser.quit()
