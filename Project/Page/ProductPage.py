from selenium.webdriver.support.select import Select

from Project.Locator.Product import Product


class ProductPage():

        def __init__(self, driver):

            self.driver = driver

            self.product = Product.product
            self.detail_product = Product.detail_product
            self.button_addtocart = Product.button_addtocart
            self.button_addtocart_2 = Product.button_addtocart_2
            self.shopping_cart_icon = Product.shopping_cart_icon
            self.product_2 = Product.product_1
            self.productname_cart = Product.product_name_cart
            self.backbutton = Product.back_button


        def click_product(self):
            self.driver.find_element("xpath", self.product).click()

        def check_detail_product(self, detail):
            self.driver.find_element("xpath",self.detail_product).text
            if  self.driver.find_element("xpath",
                    self.detail_product).text == detail:
                print("test_4_ViewProduct: Detail product is rignt")
            else:
                print("test_4_ViewProduct: Detail product is wrong")

        def addProduct_1(self):
            self.driver.find_element("xpath",self.button_addtocart).click()

        def addProduct_2(self):
            self.driver.find_element("xpath",self.button_addtocart_2).click()

        def CheckProduct(self):
            number =  self.driver.find_element("xpath",self.shopping_cart_icon).text
            if  self.driver.find_element("xpath",self.shopping_cart_icon).text >= "0":
                print("There is " + number + " product in cart")
            elif not  self.driver.find_element("xpath",self.shopping_cart_icon).text == None:
                print("There is no product in cart")
            else:
                print("error")

        def ClickProduct2(self):
            self.driver.find_element("xpath",self.product_2).click()

        def Print_Number_NameOfProduct(self):
            product =  self.driver.find_element("class-name",self.productname_homepage)
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

        def Backbutton(self):
            self.driver.find_element("xpath",self.backbutton).click()






