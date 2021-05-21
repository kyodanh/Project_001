from selenium import webdriver
import unittest
import time
from Project.Page.SigninPage import SigninPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

class SigninTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\pythonProject\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1_OpenWeb(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/") #openwweb
        driver.set_page_load_timeout(20)
        time.sleep(0.3)

    def test_2_SignIn(self):
        driver = self.driver
        signin = SigninPage(driver)
        signin.input_username("standard_user")
        time.sleep(0.3)
        signin.input_password("secret_sauce")
        time.sleep(0.3)
        signin.click_button_signin()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")
