import os, sys
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
from tkinter.messagebox import askyesno
from cookies import *
from is_logged import *
from ui_interaction import *
from upload_videos import *
from toaster import *

# Configs
CHANNEL_ID = sys.argv[1]
SESSION_NAME = sys.argv[2]
FOLDER = sys.argv[3]

if not os.path.exists(FOLDER):
    print('Diretório especificado não existe!')
    sys.exit()

# Inicia o Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = uc.Chrome(options=chrome_options)

# Navega até o YouTube
driver.get('https://youtube.com')

# Carrega os cookies e
# Se os cookies tiverem sido carregados,
# atualiza a página
cookies_loaded = load_cookies(driver, SESSION_NAME)
if cookies_loaded:
    print('COOKIES CARREGADOS!')
    driver.get('https://youtube.com')

# Se não se está logado, então é necessário
# fazer a autenticação manualmente
while not is_logged(driver):
    toaster.show_toast('Usuário não logado', 'Faça o login para prosseguir com os uploads', './icons/warning.ico', 5, True)
   
    # Se não está logado, inicia uma instância headful
    # do browser para a realização do login manual
    driver_login = uc.Chrome(options=webdriver.ChromeOptions())
    driver_login.get('https://youtube.com')
    try:
        element = WebDriverWait(driver_login, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#buttons > ytd-button-renderer > yt-button-shape > a > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill')))
    except:
        print('Erro: não foi possível realizar o login')
        continue
    element.click()
    
    if not askyesno('Faça o login', 'Aperte "sim" quando terminar de logar ou "não" para abortar o script'):
        print('Abortando...')
        sys.exit()

    # Então salva os cookies
    save_cookies(driver_login, SESSION_NAME)
    driver_login.quit()
    
    # Então os carrega na instância headless
    load_cookies(driver, SESSION_NAME)

    # E volta à página inicial (necessário para a função is_logged)
    driver.get('https://youtube.com')
    

# Faz o upload dos vídeos
try:
    upload_videos(driver, CHANNEL_ID, 10, FOLDER)
except (ElementNotInteractableException, ElementClickInterceptedException):
    toaster.show_toast(f'Erro em {SESSION_NAME}', f'É provável que o limite diário de uploads tenha sido atingido', None, 10, True)

# Avisa a finalização do script
toaster.show_toast('Uploads encerrados', f'Os uploads da sessão {SESSION_NAME} foram encerrados.', None, 10, True)


