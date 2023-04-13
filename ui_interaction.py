from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import demoji, time

def open_yt_upload_dialog(driver, CHANNEL_ID):
    driver.get(f"https://studio.youtube.com/channel/{CHANNEL_ID}/videos?d=ud")

def select_video_file(driver, video_file):
    driver.find_elements(By.CSS_SELECTOR, 'input[type=File]')[0]\
        .send_keys(video_file)

def type_video_title(driver, video_title):
    # Espera até estar tudo pronto
    while True:
        try:
            title_txtbox = driver.find_elements(By.CSS_SELECTOR, '#textbox')[0]
            break
        except: pass
    title_txtbox.clear()
    title_txtbox.clear()
    title_txtbox.clear()
    title_txtbox.clear()
    title_txtbox.clear()
    title_txtbox.send_keys(demoji.replace(video_title, ''))

def type_video_description(driver, video_description):
    # Espera até estar tudo pronto
    while True:
        try: 
            descr_txtbox = driver.find_elements(By.CSS_SELECTOR, '#textbox')[1]
            break
        except: pass
    descr_txtbox.clear()
    descr_txtbox.send_keys(demoji.replace(video_description, ''))


def check_as_not_for_children_audience(driver):
    driver.find_elements(By.CSS_SELECTOR, '#audience > ytkc-made-for-kids-select > div.made-for-kids-rating-container.style-scope.ytkc-made-for-kids-select > tp-yt-paper-radio-group > tp-yt-paper-radio-button:nth-child(2)')[0].click()

def click_next_button_3_times(driver):
    for _ in range(0, 3):
        driver.find_elements(By.CSS_SELECTOR, '#next-button')[0].click()

def check_as_public(driver):
    WebDriverWait(driver, 120).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#privacy-radios #radioContainer')))[2].click()

def click_show_more(driver):
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#toggle-button > div'))).click()

def type_tags(driver, tags):
    tags_input = driver.find_elements(By.CSS_SELECTOR, '#text-input')[1]
    tags_input.send_keys(','.join(tags))

def click_done_button(driver):
    driver.find_elements(By.CSS_SELECTOR, '#done-button')[0].click()