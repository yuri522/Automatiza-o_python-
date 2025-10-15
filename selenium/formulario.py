from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://pt.anotepad.com")
time.sleep(15)

titulo = driver.find_element(By.ID, "edit_title")
titulo.send_keys("Sou Aluno Do Senac")


titulo = driver.find_element(By.ID, "edit_textarea")
titulo.send_keys("Teste automatico")

time.sleep(20)

driver.quit()