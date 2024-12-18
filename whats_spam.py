from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def iniciar_driver():
    options = Options()
    options.add_argument('--start-maximized')
    # options.add_argument('--headless')  # Para rodar em modo headless
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver


def buscar_usuario(driver, name):
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox" and @contenteditable="true"]'))
        )
        search_box.click()
        search_box.send_keys(name)
        search_box.send_keys(Keys.ENTER)
        print(f"Usuário '{name}' localizado.")
        return True
    except TimeoutException:
        print(f"Usuário '{name}' não encontrado.")
        return False


def enviar_mensagens(driver, texto, count):
    try:
        for i in range(int(count)):
            msg_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="textbox" and @contenteditable="true"]'))
            )
            msg_box.send_keys(texto)
            msg_box.send_keys(Keys.ENTER)
            print(f"Mensagem {i + 1} enviada.")
    except TimeoutException:
        print("Erro: Campo de texto não encontrado.")


def main():
    driver = iniciar_driver()
    driver.get('https://web.whatsapp.com/')
    input('Pressione ENTER após leitura do QR Code...')

    name = input('Insira o nome do usuário ou grupo: ')
    if buscar_usuario(driver, name):
        texto = input('Conteúdo da mensagem: ')
        count = input('Quantidade de mensagens: ')
        enviar_mensagens(driver, texto, count)

    driver.quit()


if __name__ == "__main__":
    main()
