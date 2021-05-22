from selenium import webdriver
import unittest
import time

from selenium.common.exceptions import NoSuchElementException

from Project.Page.SigninPage import SigninPage
from Project.Page.HomePage import HomePage
from Project.TestCase.SignInTestCase import SigninTestCase
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

class HomepageTestCase(unittest.TestCase):

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

    def test_3_ProductPage(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.select_az()
        time.sleep(0.3)
        homepage.select_za()
        time.sleep(0.3)
        homepage.select_lohi()
        time.sleep(0.3)
        homepage.select_hilo()
        time.sleep(0.3)
        homepage.select_az()
        homepage.click_menu()

    def test_4_ViewProduct(self):
        driver = self.driver
        viewproduct = HomePage(driver)
        viewproduct.click_product()
        viewproduct.check_detail_product("carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")

    def test_5_Add_ProductToCart(self):
        driver = self.driver
        addproduct = HomePage(driver)
        addproduct.addProduct_1()


    def test_6_Check_ProductToCart(self):
        driver = self.driver
        addproduct = HomePage(driver)
        addproduct.CheckProduct()

    def test_7_Add_Other_ProductToCart(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='back-to-products']").click()
        addproduct = HomePage(driver)
        addproduct.ClickProduct2()
        addproduct.addProduct_2()
        addproduct.CheckProduct()


    def test_8_View_ProductinCart(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='shopping_cart_container']/a").click()
        product =  driver.find_elements_by_class_name("inventory_item_name")
        if  len(product) > 0 :
             for i in product:
                 print("Product in cart:" + i.text)
        else :
            print("There is no product in cart")





    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")
