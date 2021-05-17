from bs4 import BeautifulSoup
import json
import os
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# for headless browsing
from selenium.webdriver.firefox.options import Options

def read_from_json_file(key):
    path = os.path.join(settings.BASE_DIR, 'shareApi/config.json')
    with open(path) as f:
        data = json.load(f)
    return data['credentials'][key]


def send_request():
    url = read_from_json_file('url')
    page = ''
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    delay = 3 # seconds
    while True:
        try:
            WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'companyShare')))
            page = BeautifulSoup(browser.page_source, 'html.parser')
            break
        except TimeoutException:
            print('loading took too much time!')
        finally:
            browser.close()
    return page
    

def extract_share_page():
    page = send_request()
    select_tag = page.find("select")
    options = select_tag.find_all("option")
    for option in options:
        print('--------------------------')
        print(option.text)
        print(option['value'])
        print('--------------------------')
    return 1
