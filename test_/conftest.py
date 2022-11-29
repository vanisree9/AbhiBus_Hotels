import pytest
from selenium import webdriver
from Library.config import Config
# path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\chromedriver.exe"
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options

#Cross Browsing
# firefox_Driver_path = r"C:\Users\harsh\Downloads\chromedriver_win32 (1)\geckodriver.exe"
@pytest.fixture(params=["Chrome","Edge"])
def _driver(request):



    # if request.param == "Firefox":
    #     pass
    #     #  options = Options()
    #     #  options.binary_location= r'C:\Program Files\Mozilla Firefox\firefox.exe'
    #     #  driver = webdriver.Firefox(executable_path=firefox_Driver_path,options=options)




    if request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_Driver_Path)

    elif request.param == "Chrome":
        driver = webdriver.Chrome(Config.ChromePath_Driver_Path)



    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    print(driver.title)
    # driver.save_screenshot("text_loginpage.png")
    driver.close()