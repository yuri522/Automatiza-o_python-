from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://automatizado.netlify.app")
time.sleep(7)

time.sleep(5)
driver.maximize_window()

input_nome = driver.find_element(By.ID, 'nome')
input_nome.send_keys("Ga bunda rachada")

time.sleep(4)
input_email = driver.find_element(By.ID, 'email')
input_email.send_keys("Ga@gmail.com")

time.sleep(4)
input_telefone = driver.find_element(By.ID, 'telefone')
input_telefone.send_keys("18 21517 1451")

time.sleep(4)
input_nascimento = driver.find_element(By.ID, 'nascimento')
input_nascimento.send_keys("02092000 ")

time.sleep(5)
input_cpf = driver.find_element(By.ID, 'cpf')
input_cpf.send_keys("32131831-21 ")

time.sleep(6)
input_cep = driver.find_element(By.ID, 'cep')
input_cep.send_keys("312313-22 ")

time.sleep(5)
input_endereco = driver.find_element(By.ID, 'endereco')
input_endereco.send_keys("R.Alameda, avenida caramba  10 Casa ")


time.sleep(5)
input_cidade = driver.find_element(By.ID, 'cidade')
input_cidade.send_keys("São Paulo")

time.sleep(5)
input_estado = driver.find_element(By.ID, 'estado')
for _ in range(25):
    input_estado.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)
input_estado.send_keys(Keys.ENTER)

time.sleep(5)
input_observacao = driver.find_element(By.ID, 'observacoes')
input_observacao.send_keys("Automatizando essa bodegaaaaa")

time.sleep(5)
input_salvar = driver.find_element(By.TAG_NAME, 'button')
input_salvar.send_keys(Keys.ENTER)

time.sleep(3)

driver.quit()
