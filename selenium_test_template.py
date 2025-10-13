import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string

class GoogleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() # Make sure you have chromedriver installed and in PATH
        self.driver.implicitly_wait(10)

    def test_open_google(self):
        driver = self.driver
        driver.get("https://www.google.com")
        assert "Google" in driver.title

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
