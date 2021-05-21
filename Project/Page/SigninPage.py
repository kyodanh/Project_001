from Project.Locator.Signin import Signin
class SigninPage():

    def __init__(self, driver):

        self.driver = driver

        self.username = Signin.username
        self.password = Signin.password
        self.button_signin = Signin.button_signin

    def input_username(self,username):
        self.driver.find_element_by_xpath(self.username).clear()
        self.driver.find_element_by_xpath(self.username).send_keys(username)

    def input_password(self,password):
        self.driver.find_element_by_xpath(self.password).clear()
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def click_button_signin(self):
        self.driver.find_element_by_xpath(self.button_signin).click()

