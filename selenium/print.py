from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(3)
driver.save_screenshot("Site_python.png")

driver.qui()