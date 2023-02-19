import time

from behave import *
from selenium import webdriver


@given(u'Thực hiện mở trang web')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


@when(u'Thực hiện nhập thông tin username và password')
def step_impl(context):
    context.driver.find_element("xpath","//*[@id='user-name']").send_keys("standard_user")
    time.sleep(2)
    context.driver.find_element("xpath","//*[@id='password']").send_keys("secret_sauce")
    time.sleep(2)



@then(u'bấn vào nut login')
def step_impl(context):
    context.driver.find_element("xpath","//*[@id='login-button']").click


@when(u'Thực hiện nhập thông tin username "{username}" và password "{password}"')
def step_impl(context,username,password):
    context.driver.find_element("xpath", "//*[@id='user-name']").send_keys(username)
    time.sleep(2)
    context.driver.find_element("xpath", "//*[@id='password']").send_keys(password)
    time.sleep(2)


@then(u'kiểm tra màn hình có chữ login hay không')
def step_impl(context):
    context.driver.close()