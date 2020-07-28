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

        # Signs into LinkedIn with given creditentials  

        self.username = username
        self.password = password

        self.driver.get(self.login)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

        # Gets web content from a linkedIn List pretaining to a specific job search.
        

        # Accesses the website and assigns the data to a variable
        

app1 = TalentSearch(username='amariawest@gmail.com', password='Tealsoap35')
