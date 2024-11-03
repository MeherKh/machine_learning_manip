## Ne pas oublier d'installer ces packages
# pip install selenium
# pip install webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

## il faut placer le dossier du driver dans ce folder
## init le driver(le navigateur headless)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# ou bien
#driver = webdriver.Chrome()

## visiter un url
url = "https://www.selenium.dev/selenium/web/web-form.html"
driver.get(url)

## patienter pendant 5s
time.sleep(5)

# fermer le navigateur
driver.quit()