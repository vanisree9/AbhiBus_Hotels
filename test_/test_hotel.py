import time
import pytest
from POM.hotel_module import Hotels

# class Test_Hotel:
#     def test_hotel(self,_driver):
#         result=Hotel(_driver)
#         time.sleep(2)
#         result.open_Hotelpage()
#         time.sleep(2)
#         result.for_place()
#         time.sleep(5)
#         result.for_checkin_checkout()
#         time.sleep(5)
#         result.for_adults_children_rooms()
#         time.sleep(2)
#         result.for_select_checkbox()
#         time.sleep(2)
#         result.for_submit()
#         time.sleep(2)
#         result.for_select_hotel()
#         time.sleep(2)
#         result.for_reserve()
#         time.sleep(2)
###########################################
class Test_hotels:
    @pytest.mark.parametrize("place_",[("pune"),("123")])
    def test_hotels(selfself,_driver,place_):
        result=Hotels(_driver)
        time.sleep(2)
        result.hotelIcon()
        time.sleep(2)
        result.forPlace(place_)
        time.sleep(10)
        result.checkIn()
        time.sleep(2)
        result.checkAdult()
        time.sleep(4)
        result.checkChild()
        time.sleep(2)
        result.checkRoom()
        time.sleep(2)
        result.checkBox()
        time.sleep(2)
        result.searchButton()
        time.sleep(2)
        result.selectHotel()
        time.sleep(10)
        result.reserveHotel()
        time.sleep(5)




