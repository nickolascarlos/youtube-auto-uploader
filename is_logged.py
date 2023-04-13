from selenium.webdriver.common.by import By
from datetime import *
import time

def is_logged(driver):
    # Verifica a existência de um elemento
    # que só existe quando se está logado
    print('Verificando se está logado...')
    first_try = datetime.now()
    while True:
        if (datetime.now() - first_try).seconds > 10:
            return False
        try:
            driver.find_elements(By.CSS_SELECTOR, '.yt-spec-icon-badge-shape__icon')[0]
            return True
        except:
            time.sleep(1)