from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class jackets(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.supremenewyork.com/shop/all/jackets")

    def search(self):
        style = driver.find_element_by_case('name-link')
        color = driver.find_element_by_case('name-link')