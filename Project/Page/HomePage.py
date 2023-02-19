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
        self.productname_homepage = Home.product_name_homepage
        self.productname_cart = Home.product_name_cart
        self.shopping_cart_icon = Home.shopping_cart_icon




    def select_az(self):
        select = Select(self.driver.find_element("xpath",self.select_box))
        select.select_by_value(self.az)

    def select_za(self):
        select = Select(self.driver.find_element("xpath",self.select_box))
        select.select_by_value(self.za)

    def select_lohi(self):
        select = Select(self.driver.find_element("xpath",self.select_box))
        select.select_by_value(self.lohi)

    def select_hilo(self):
        select = Select(self.driver.find_element("xpath",self.select_box))
        select.select_by_value(self.hilo)

    def click_menu(self):
        self.driver.find_element("xpath",self.menu).click()

    def Print_Number_NameOfProduct(self):
        product = self.driver.find_element("class-name",self.productname_homepage)
        if len(product) > 0:
            count = len(product)
            print("There are ", count, " Items")
            for (item, i) in enumerate(product, start=1):
                print("Product", item, "in Product Page:" + i.text)
        else:
            print("There is no Product Page")

    def ClickCart(self):
        self.driver.find_element("xpath",self.shopping_cart_icon).click()

    def Print_Number_NameOfCart(self):
        product = self.driver.find_element("class-name",self.productname_cart)
        if len(product) > 0:
            count = len(product)
            print("There are ", count, " Items")
            for (item, i) in enumerate(product, start=1):
                print("Product", item, "in in cart:" + i.text)
        else:
            print("There is no product in cart")






