import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UserLogIn(unittest.TestCase):
    def setUp(self):
        self.url = "https://account.bbc.com"
        self.driver = webdriver.Chrome(executable_path='seleniumdrivers/chromedriver.exe')

    def test_invalid_login(self):
        driver = self.driver
        driver.get(self.url)
        username = driver.find_element_by_id("user-identifier-input")
        password = driver.find_element_by_id("password-input")
        login = driver.find_element_by_id("submit-button")
        username.send_keys("lahariuudi@gmail.com")
        password.send_keys("bbc@BBC@")
        login.send_keys(Keys.RETURN)
        assert "we can’t find an account" in driver.page_source

    def test_valid_login(self):
        driver = self.driver
        driver.get(self.url)
        beforelogintitle=driver.title
        username = driver.find_element_by_id("user-identifier-input")
        password = driver.find_element_by_id("password-input")
        login = driver.find_element_by_id("submit-button")
        username.send_keys("laharimullapudi@gmail.com")
        password.send_keys("bbc@BBC@")
        login.send_keys(Keys.RETURN)
        afterlogintitle = driver.title
        self.assertNotEqual(beforelogintitle,afterlogintitle)
        driver.delete_all_cookies()

    def tearDown(self):
        self.driver.close()

