from selenium import webdriver
import time
path=r"C:\Users\harsh\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver=webdriver.Chrome(path)
# driver.get("https://www.abhibus.com/")
# driver.maximize_window()
driver.implicitly_wait(30)
from Data import reading_objects
Hotel_object=reading_objects.read_locators()
print(Hotel_object)

# class Hotel:
#     def __init__(self,_driver):
#         self.driver=_driver
#     def open_Hotelpage(self):
#         self.driver.find_element(*Hotel_object['open_hotels']).click()
#         time.sleep(2)
#     def for_place(self):
#         time.sleep(5)
#         self.driver.find_element(*Hotel_object["for_where are you going"]).send_keys("Pune")
#         time.sleep(5)
#         self.driver.find_element(*Hotel_object["for_place"]).click()
#         time.sleep(5)
#     def for_checkin_checkout(self):
#         self.driver.find_element(*Hotel_object["for_checkin"]).click()
#         time.sleep(10)
#         self.driver.find_element(*Hotel_object["for_checkin_date"]).click()
#         # self.driver.find_element("xpath","//form[@id='frm']").click()
#         # time.sleep(10)
#         # self.driver.find_element("xpath","//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[2]/table/tbody/tr[4]/td[4]").click()
#         time.sleep(10)
#         self.driver.find_element(*Hotel_object["for_date"]).click()
#         time.sleep(5)
#         self.driver.find_element(*Hotel_object["for_checkout_date"]).click()
#         time.sleep(5)
#     def for_adults_children_rooms(self):
#         self.driver.find_element(*Hotel_object["for_adults"]).click()
#         time.sleep(2)
#         self.driver.find_element(*Hotel_object["for_adults_increment"]).click()
#         time.sleep(2)
#         self.driver.find_element(*Hotel_object["for_children"])
#         time.sleep(2)
#         self.driver.find_element(*Hotel_object["for_rooms"]).click()
#         time.sleep(2)
#         self.driver.find_element(*Hotel_object["for_rooms_increment"]).click()
#         time.sleep(2)
#     def for_select_checkbox(self):
#         self.driver.find_element(*Hotel_object["for_select_checkbox"]).click()
#         time.sleep(2)
#     def for_submit(self):
#         self.driver.find_element(*Hotel_object["for_submit"]).click()
#         time.sleep(2)
#     def for_select_hotel(self):
#         self.driver.find_element(*Hotel_object["for_select_hotel"]).click()
#         time.sleep(2)
#         handles = self.driver.window_handles
#         time.sleep(1)
#         self.driver.switch_to.window(handles[1])
#     def for_reserve(self):
#         self.driver.find_element(*Hotel_object["for_reserve"]).click()
#         time.sleep(2)

# result=Hotel(driver)
# result.open_Hotelpage()
# result.for_place()
# result.for_checkin_checkout()
# result.for_adults_children_rooms()
# result.for_select_checkbox()
# result.for_submit()
# result.for_select_hotel()
# result.for_reserve()
##################################
class Hotels:
    def __init__(self, driver):
        self.driver=driver
    def hotelIcon(self):
        self.driver.find_element(*Hotel_object["open_hotels"]).click()
        time.sleep(2)
    def forPlace(self,place_):
        self.driver.find_element(*Hotel_object["for_where are you going"]).send_keys(place_)
        time.sleep(10)
        self.driver.find_element(*Hotel_object["for_place"]).click()
        # self.driver.find_element("xpath", '//li[@data-i="0"]').click()
        time.sleep(10)
    def checkIn(self):
        self.driver.find_element(*Hotel_object["for_checkin"]).click()
        time.sleep(2)
        self.driver.find_element(*Hotel_object["for_checkin_date"]).click()
        time.sleep(2)
        self.driver.find_element(*Hotel_object["for_date"]).click()
        time.sleep(2)
        self.driver.find_element(*Hotel_object["for_checkout_date"]).click()
        time.sleep(5)
    def checkAdult(self):
        self.driver.find_element(*Hotel_object["for_adults"]).click()
        time.sleep(3)
        self.driver.find_element(*Hotel_object["for_adults_increment"]).click()
        time.sleep(3)
    def checkChild(self):
        self.driver.find_element(*Hotel_object["for_children"])
        time.sleep(2)
    def checkRoom(self):
        self.driver.find_element(*Hotel_object["for_rooms"]).click()
        self.driver.find_element(*Hotel_object["for_rooms_increment"]).click()
        time.sleep(2)
    def checkBox(self):
        self.driver.find_element(*Hotel_object["for_select_checkbox"]).click()
        time.sleep(2)
    def searchButton(self):
        self.driver.find_element(*Hotel_object["for_submit"]).click()
        time.sleep(5)
    def selectHotel(self):
        self.driver.find_element(*Hotel_object["for_select_hotel"]).click()
        time.sleep(2)
        handles = self.driver.window_handles
        time.sleep(3)
        self.driver.switch_to.window(handles[1])
    def reserveHotel(self):
        self.driver.find_element(*Hotel_object["for_reserve"]).click()
        time.sleep(10)
# result=Hotels(driver)
# result.hotelIcon()
# result.forPlace()
# result.checkIn()
# result.checkAdult()
# result.checkChild()
# result.checkRoom()
# result.checkBox()
# result.searchButton()
# result.selectHotel()
# result.reserveHotel()
