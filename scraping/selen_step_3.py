import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


## il faut placer le dossier du driver dans ce folder
## init le driver(le navigateur headless)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

## visiter un url
url = "https://www.selenium.dev/selenium/web/web-form.html"
driver.get(url)

## extraire le titre
title = driver.title

## La synchronisation du code avec l'état actuel du navigateur est l'un des plus grands défis 
## Essentiellement, vous voulez vous assurer que l'élément est sur la page avant d'essayer de le localiser 
## et que l'élément est dans un état interactif avant d'essayer d'interagir avec lui.
driver.implicitly_wait(0.5)
## ou bien avec time.sleep(0.5)

## Chercher un element par son nom
text_box = driver.find_element(by=By.NAME, value="my-text")
## ou bien par l'ID
text_box = driver.find_element(by=By.ID, value="my-text-id")

## ou bien par la classe
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
## Note: pour extraire plusieurs balises comme en BS4
## on peut utiliser `find_elements`
## => `find_element` -> un seul element
## => `find_elements` -> liste d'elements

## Ecrire sur le text_box
time.sleep(4)
text_box.send_keys("Hello")
time.sleep(5)

## effacer
text_box.clear()
time.sleep(5)

## ecrire de nouveau
text_box.send_keys("Hello")
time.sleep(5)

## tester si le checked box est selectionné ?
check_box_1 = driver.find_element(by=By.ID, value="my-check-1")
print("le check box 1 est :", "enabled" if check_box_1.is_enabled() else "not enabled")
check_box_2 = driver.find_element(by=By.ID, value="my-check-2")
print("le check box 2 est :", "selected" if check_box_2.is_selected() else "not selected")

## cliquer sur submit
submit_button.click()

## extraire le message apres submit
message = driver.find_element(by=By.ID, value="message")
print("le message : ", message.text)

time.sleep(10)
## fermer le navigateur
driver.quit()
