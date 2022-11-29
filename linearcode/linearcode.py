from selenium import webdriver
from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains  import ActionChains
import time
path=r"C:\Users\harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://www.abhibus.com/")
driver.maximize_window()
driver.implicitly_wait(30)
### open to hotel page
driver.find_element("xpath","//a[@class='nav-link bg-gray rounded-pill px-4 py-1']").click()
time.sleep(2)
## Enter  for  where are you going
for_=driver.find_element("xpath",'//input[@placeholder="Where are you going?"]')
for_.click()
for_.send_keys("Pune")
time.sleep(5)
driver.find_element("xpath",'//li[@data-i="0"]').click()
time.sleep(2)
##  for checkin and checkout
driver.find_element("xpath","//*[@id='frm']").click()
time.sleep(2)
driver.find_element("xpath","(//span[@class='sb-date-field__icon sb-date-field__icon-btn bk-svg-wrapper calendar-restructure-sb'])[1]").click()
time.sleep(2)
driver.find_element("xpath",'(//td[@role="gridcell"])[50]').click()
time.sleep(5)
driver.find_element("xpath",'(//td[@role="gridcell"])[52]').click()
time.sleep(5)
# To click on adults
driver.find_element("xpath","//span[text()='2 adults']").click()
time.sleep(2)
driver.find_element("xpath","(//span[text()='+'])[1]").click()
time.sleep(2)
# To click on children
driver.find_element("xpath","//span[text()='0 children']")
time.sleep(2)
# To click on rooms
driver.find_element("xpath","//span[text()='1 room']").click()
driver.find_element("xpath","(//span[text()='+'])[3]").click()
time.sleep(2)
# To select the checkbox
driver.find_element("xpath","//label[@class='bui-checkbox__label']").click()
time.sleep(2)
# To click on search button
driver.find_element("xpath","//span[@class='js-sb-submit-text  b-button__text']").click()
time.sleep(5)
# To select for hotel
driver.find_element("xpath","//div[text()='Four Points by Sheraton Hotel and Serviced Apartments Pune']").click()
time.sleep(2)
handles = driver.window_handles
time.sleep(1)
driver.switch_to.window(handles[1])
# To click on reserve
driver.find_element("xpath","//*[@id='hcta']/span[1]").click()

