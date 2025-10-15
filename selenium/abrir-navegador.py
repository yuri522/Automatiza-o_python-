from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

caixa_pesquisa = driver.find_element(By.NAME, 'q')
caixa_pesquisa.send_keys("Python")
caixa_pesquisa.send_keys(Keys.ENTER)

time.sleep(5)

driver.maximize_window()

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)


driver.refresh()
time.sleep(3)

time.sleep(12)

driver.minimize_window()

time.sleep(8)

driver.quit()