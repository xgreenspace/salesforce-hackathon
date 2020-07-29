import configparser
import json
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

        self.driver.get(self.search_people)
        search = self.driver.find_element_by_class_name('search-global-typeahead__input')
        search.send_keys(job)
        search.send_keys(Keys.ENTER)

        time.sleep(3)
        # Looks through each listing
        
        profiles = []

        max_page = 1
        for current_page in range(max_page):
            names = self.driver.find_elements_by_xpath('//*[@class="search-result__result-link ember-view"]')
            print(names)
            for name in names:
                print(name.get_attribite('href'))



with open('auth.json', 'r') as f:
    credentials = json.load(f)

username = credentials['username']
password = credentials['password']

app1 = TalentSearch(job='Nurse', username=username, password=password)
