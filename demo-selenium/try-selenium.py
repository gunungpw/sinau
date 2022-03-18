import imp
from selenium import webdriver
import time

driver_path = "C:/chromedriver_win32/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser.get("https://www.monkeytype.com")

time.sleep(5)
browser.quit()
