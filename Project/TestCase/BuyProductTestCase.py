from selenium import webdriver
import unittest
import time

from selenium.common.exceptions import NoSuchElementException

from Project.Page.SigninPage import SigninPage
from Project.Page.HomePage import HomePage
from Project.Page.ProductPage import ProductPage
from Project.TestCase.SignInTestCase import SigninTestCase
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

class BuyProductCase(unittest.TestCase):

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
        homepage.Print_Number_NameOfProduct()
        homepage.click_menu()

    def test_4_ViewProduct(self):
        driver = self.driver
        viewproduct = ProductPage(driver)
        viewproduct.click_product()
        viewproduct.check_detail_product("carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")

    def test_5_Add_ProductToCart(self):
        driver = self.driver
        addproduct = ProductPage(driver)
        addproduct.addProduct_1()


    def test_6_Check_ProductToCart(self):
        driver = self.driver
        addproduct = ProductPage(driver)
        addproduct.CheckProduct()

    def test_7_Add_Other_ProductToCart(self):
        driver = self.driver
        addproduct = ProductPage(driver)
        addproduct.Backbutton()
        addproduct.ClickProduct2()
        addproduct.addProduct_2()
        addproduct.CheckProduct()

    def test_8_View_ProductinCart(self):
        driver = self.driver
        viewcart = ProductPage(driver)
        viewcart.ClickCart()
        viewcart.Print_Number_NameOfCart()

    def test_9_1_Checkout(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='checkout']").click()
        driver.find_element_by_xpath("//*[@id='first-name']").send_keys("test")
        driver.find_element_by_xpath("//*[@id='last-name']").send_keys("test")
        driver.find_element_by_xpath("//*[@id='postal-code']").send_keys("test")
        driver.find_element_by_xpath("//*[@id='continue']").click()

    def test_9_2_CheckOut_OverView(self):
        driver = self.driver
        product = driver.find_elements_by_class_name("inventory_item_name")
        if len(product) > 0:
            count = len(product)
            print("There are ", count, " Items")
            for (item, i) in enumerate(product, start=1):
                print("Product", item, "in in cart:" + i.text)
        else:
            print("There is no product in cart")

        payment = driver.find_element_by_xpath("//*[@id='checkout_summary_container']/div/div[2]/div[2]").text
        if payment == "SauceCard #31337" :
            print("Payment Information : " ,payment)
        else:
            print("no")

        shipping = driver.find_element_by_xpath("//*[@id='checkout_summary_container']/div/div[2]/div[4]").text
        if shipping == "FREE PONY EXPRESS DELIVERY!":
            print("Shipping Information: ", shipping)
        else:
            print("no")

        Item  = driver.find_element_by_xpath("//*[@id='checkout_summary_container']/div/div[2]/div[5]").text
        if Item  == "Item total: $39.98":
            print(Item)
        else:
            print("no")

        Tax = driver.find_element_by_xpath("//*[@id='checkout_summary_container']/div/div[2]/div[6]").text
        if Tax == "Tax: $3.20":
            print(Tax)
        else:
            print("no")

        Total = driver.find_element_by_xpath("//*[@id='checkout_summary_container']/div/div[2]/div[7]").text
        if Total == "Total: $43.18":
            print(Total)
        else:
            print("no")

    def test_9_3_finish_CheckOut(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='finish']").click()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")
