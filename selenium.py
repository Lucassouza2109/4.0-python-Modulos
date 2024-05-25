# type: ignore
# ACIMA - VAI IGNORAR A TIPAGEM NO ARQUIVO. 

# Selenium - Automatizando tarefas no navegador


from pathlib import Path
# PARA TRABALHAR COM CAMINHO. 

from time import sleep
# PARA NAO FECHAR O BROWSER RAPIDO

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# UTILIZADO PARA SELECIONAR UM COMANDO. 
from selenium.webdriver.common.keys import Keys
# ME PERMITE ENVIAR VARIAS TECLAS - COMANDO, PARA O MEU CODIGO.
from selenium.webdriver.support import expected_conditions as EC
# FAZ COM QUE A EXECUCAO TENHA UMA CONDICAO ESPERADA.
from selenium.webdriver.support.wait import WebDriverWait
# VAI REALIZAR A ESPERA DO COMANDO. 


# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raiz do projeto :
ROOT_FOLDER = Path(__file__).parent

# Caminho para a pasta onde o chromedriver está:
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

# Depuracao:
print (f' ChromeDriver Path: {CHROME_DRIVER_PATH}')

def make_chrome_browser(*options: str) -> webdriver.Chrome:

# CHROME OPTIONS / SERVICE / BROWSER = OPCOES DE COMO ABRIR O NAVEGADOR. 
# OPTIONS = CONFIGURACOES
# SERVICE = QUAL O SERVICO QUE VAI UTILIZAR P CHROMEDRIVER
# BROWSER = NAVEGADOR

    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10 # VAI ESPERAR UM COMANDO APARECER NA TELA. 

    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes:
    # NAVEGADOR VAI ABRIR O SITE ABAIXO.
    browser.get('https://www.google.com')


    # Espere para encontrar o input:
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    # ACIMA, AO ABRIR O NAVEGADOR, ELE VAI AGUARDAR ATE A CONDICAO : 
    # QUE O ELEMENTO ESTEJA NA TELA - (By.NAME, 'q')

    search_input.send_keys('Hello World!')
    # SENDO ENCONTRADA A CONDICAO ELE VAI DIGITAR NA TELA - ('Hello World!')
    search_input.send_keys(Keys.ENTER)
    # APOS DIGITAR ELE VAI DAR ENTER E COM ISSO REALIZAR A BUSCA NO GOOGLE.

    # --------------
    # AGORA -- Tendo certeza que o objeto procurado vai estar na Tela : 
    results = browser.find_element(By.ID, 'search')
    # find_element (1 elemento) - Pega o search.
    links = results.find_elements(By.TAG_NAME, 'a')
    # em results, eu vou pegar os elementos por TAG_NAME e selecionar a Tag : a.
    links[0].click()
    # No elemento 0, eu dou o comando = click.

    # ----------------

    # Dorme por 10 segundos:
    sleep(TIME_TO_WAIT)