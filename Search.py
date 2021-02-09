import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchFunctionality(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.bbc.co.uk/search"
        self.driver = webdriver.Chrome(executable_path='seleniumdrivers/chromedriver.exe')

    def test_valid_search(self):
        driver = self.driver
        driver.get(self.url)
        searchbox = driver.find_element_by_xpath("//*[@id='search-input']")
        searchbox.send_keys("vaccine")
        searchbox.send_keys(Keys.RETURN)
        sleep(1)
        allelements = driver.find_elements_by_xpath("//*[@id='main-content']/div/div[3]/div/div/ul/li/descendant::a/span")
        print(len(allelements))
        for i in allelements:
            assert "vaccine" in i.text.lower()
            print(i.text)