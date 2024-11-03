import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

## il faut placer le dossier du driver dans ce folder
## init le driver(le navigateur headless)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

## visiter un url
url = "https://www.selenium.dev/selenium/web/web-form.html"
driver.get(url)

## extract title
title = driver.title
current_url = driver.current_url
print("title:", title)
print("current_url:", current_url)
print("###########################")
time.sleep(5) ## ne rien faire pour 5 sec

## visiter une autre page
driver.get("https://www.selenium.dev/selenium/web/index.html")
print("title:", driver.title)
print("current_url aprés le changement du lien:", driver.current_url)
print("###########################")
time.sleep(5) ## ne rien faire pour 5 sec

## retourner vers la premiere page
driver.back()
print("current_url aprés le retour:", driver.current_url)
print("###########################")
time.sleep(5) ## ne rien faire pour 5 sec

## aller vers l'avant
driver.forward()
print("current_url aprés forward:", driver.current_url)
print("###########################")
time.sleep(5) ## ne rien faire pour 5 sec

## actualiser la page
driver.refresh()
print("###########################")
time.sleep(5) ## ne rien faire pour 5 sec

# fermer le navigateur
driver.quit()
print("Je Quitte")