from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
driver.maximize_window()

input('Pressione ENTER após leitura do QRCODE...')

name = input('Insira nome de usuario ou grupo: ')

# Procura por usuario
try:
    user = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]/span/span'.format(name))))
    user.click()
except:
    print("Usuario", name, "não encontrado")

# Envia conteudo
try:
    count = input("Quantidade: ")
    texto = input("Conteudo: ")
    for i in range(count):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]' ))).send_keys(texto)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button/span' ))).click()
except:
    print("Campo de texto não encontrado")
