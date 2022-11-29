from behave import *
from selenium import webdriver
import time

@given(u'Open the chrome browser')
def step_impl(context):
    path = r"C:\Users\harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe"
    context.driver = webdriver.Chrome(path)


@when(u'Enter the URL')
def step_impl(context):
    context.driver.get("https://www.abhibus.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)


@given(u'Click on hotel icon')
def step_impl(context):
    context.driver.find_element("xpath", "//a[@class='nav-link bg-gray rounded-pill px-4 py-1']").click()


@when(u'Click on ForPlace')
def step_impl(context):
    for_ = context.driver.find_element("xpath", '//input[@placeholder="Where are you going?"]')
    for_.click()
    for_.send_keys("Pune")
    time.sleep(2)
    context.driver.find_element("xpath", '//li[@data-i="0"]').click()
    time.sleep(2)


@then(u'Date selection')
def step_impl(context):
    context.driver.find_element("xpath", "//*[@id='frm']").click()
    time.sleep(2)
    context.driver.find_element("xpath","(//span[@class='sb-date-field__icon sb-date-field__icon-btn bk-svg-wrapper calendar-restructure-sb'])[1]").click()
    time.sleep(2)
    context.driver.find_element("xpath", '(//td[@role="gridcell"])[50]').click()
    time.sleep(2)
    context.driver.find_element("xpath", '(//td[@role="gridcell"])[52]').click()
    time.sleep(2)


@then(u'Select the Checkbox')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='2 adults']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "(//span[text()='+'])[1]").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//span[text()='0 children']")
    time.sleep(2)
    context.driver.find_element("xpath", "//span[text()='1 room']").click()
    time.sleep(2)
    context.driver.find_element("xpath", "(//span[text()='+'])[3]").click()
    time.sleep(2)
    context.driver.find_element("xpath", "//label[@class='bui-checkbox__label']").click()
    time.sleep(2)


@then(u'Click on search button')
def step_impl(context):
    context.driver.find_element("xpath", "//span[@class='js-sb-submit-text  b-button__text']").click()
    time.sleep(2)

@then(u'click on reserve')
def step_impl(context):
    context.driver.find_element("xpath", "//div[text()='Four Points by Sheraton Hotel and Serviced Apartments Pune']").click()
    handles = context.driver.window_handles
    context.driver.switch_to.window(handles[1])
    context.driver.find_element("xpath", "//*[@id='hcta']/span[1]").click()
    time.sleep(2)

