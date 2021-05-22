from selenium.webdriver.support.select import Select

from Project.Locator.Home import Home
class HomePage():

    def __init__(self, driver):

        self.driver = driver

        self.select_box = Home.select_box
        self.az = Home.select_az
        self.za = Home.select_za
        self.lohi = Home.select_lohi
        self.hilo = Home.select_hilo
        self.menu = Home.menu
        self.product = Home.product
        self.detail_product = Home.detail_product
        self.button_addtocart = Home.button_addtocart
        self.button_addtocart_2 = Home.button_addtocart_2
        self.shopping_cart_icon = Home.shopping_cart_icon
        self.product_2 = Home.product_1


    def select_az(self):
        select = Select(self.driver.find_element_by_xpath(self.select_box))
        select.select_by_value(self.az)

    def select_za(self):
        select = Select(self.driver.find_element_by_xpath(self.select_box))
        select.select_by_value(self.za)

    def select_lohi(self):
        select = Select(self.driver.find_element_by_xpath(self.select_box))
        select.select_by_value(self.lohi)

    def select_hilo(self):
        select = Select(self.driver.find_element_by_xpath(self.select_box))
        select.select_by_value(self.hilo)

    def click_menu(self):
        self.driver.find_element_by_xpath(self.menu).click()

    def click_product(self):
        self.driver.find_element_by_xpath(self.product).click()

    def check_detail_product(self,detail):
        self.driver.find_element_by_xpath(self.detail_product).text
        if  self.driver.find_element_by_xpath(
                self.detail_product).text == detail:
            print("test_4_ViewProduct: Detail product is rignt")
        else:
            print("test_4_ViewProduct: Detail product is wrong")

    def addProduct_1(self):
        self.driver.find_element_by_xpath(self.button_addtocart).click()

    def addProduct_2(self):
        self.driver.find_element_by_xpath(self.button_addtocart_2).click()

    def CheckProduct(self):
        number = self.driver.find_element_by_xpath(self.shopping_cart_icon).text
        if self.driver.find_element_by_xpath(self.shopping_cart_icon).text >= "0":
            print("There is " + number + " in cart")
        elif not self.driver.find_element_by_xpath(self.shopping_cart_icon).text == None :
            print("There is no product in cart")
        else :
            print("error")

    def ClickProduct2(self):
        self.driver.find_element_by_xpath(self.product_2).click()
