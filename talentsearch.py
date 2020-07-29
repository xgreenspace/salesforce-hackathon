import configparser
import json
import os
import sys
import time

import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from candidates import *


class TalentSearch():
    def __init__(self, job='', username='', password=''):

        # Initialize chromedriver and creates username and password
        self.driver = webdriver.Chrome('chromedriver/chromedriver.exe')

        self.base = 'https://www.linkedin.com'
        self.login = self.base + '/login'
        self.feed = self.base + '/feed'
        self.search_people = self.base + '/search/results/all/?keywords='

        self.sign_in(username, password)
        self.search_listings(job)
        
        # Ends Process

        time.sleep(5)
        self.driver.close()

    def sign_in(self, username, password):

        # Signs into LinkedIn with given creditentials and open search

        self.username = username
        self.password = password

        self.driver.get(self.login)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

    def search_listings(self, job):

        # Gets web content from a linkedIn List pretaining to a specific job search.
        try:
            self.driver.get(self.search_people)
            search = self.driver.find_element_by_class_name('search-global-typeahead__input')
            search.send_keys(job)
            search.send_keys(Keys.ENTER)
            time.sleep(1)
        except:
            print('Bots cannot access this account right now... Try again later! :(')
            quit()

        for i in np.arange(0, 1, .1):
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight*{})".format(i))
        
        # Looks through each listing

        profiles = []
        max_page = 1

        for current_page in range(max_page):
            # names = self.driver.find_elements_by_xpath('//*[@class="search-result__result-link ember-view"]')
            results = self.driver.find_elements_by_class_name('search-result__result-link')
            names = ['']
            for result in results:
                name = result.text.strip()
                if self.is_valid_name:

                    # Find's the names of the listings

                    try:
                        name = name[:name.index('\n')]
                        print(name)
                        names.append(name)
                    except ValueError:
                        print(name)
                        names.append(name)

                    # Open Profile of Listing
                    print(result.get_attribute('href'))
                    link = result.get_attribute('href')

                    self.driver.execute_script("window.open('');")
                    self.driver.switch_to_window(self.driver.window_handles[1])
                    self.driver.get(link)

                    profiles.append(Candidate(self.scan_profile(name, link)))

                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])
                
                # Moves on to the next page
                self.driver.find_element_by_class_name('artdeco-button__text').click()
                
    
    def scan_profile(self, name, link):
        summary = self.driver.find_element_by_class_name('pv-about__summary-text').text
        current_role = self.driver.find_element_by_class_name('mt1').text

        return (name, link, summary, current_role)


    def is_valid_name(self, name, names):
        return name and name[:name.find('\n')] != names[-1] and 'LinkedIn Member'





                    



with open('auth.json', 'r') as f:
    credentials = json.load(f)

username = credentials['username']
password = credentials['password']

app1 = TalentSearch(job='Nurse', username=username, password=password)
