from selenium import webdriver
import time


driver=webdriver.Chrome()
driver.get("http://frankenfiction.com/sad-people-like-poetry-penny-dreadful-frankenstein-romantics/")
time.sleep(5)
driver.quit()
