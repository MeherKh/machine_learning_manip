#!pip install fake-useragent
import time
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

### pageLoadStrategy avec selenium
### il existe 3 :
### 1. normal : Utilisé par défaut, attend que toutes les ressources soient téléchargées
### 2. eager: L'accès DOM est prêt, mais d'autres ressources comme les images peuvent encore être en cours de chargement
### 3. none: Ne bloque pas le WebDriver

## timeouts
### Spécifie quand interrompre l'exécution d'un script dans un contexte de navigation en cours.
### Script Timeout : Le délai d'expiration par défaut de 30 000 est imposé lorsqu'une nouvelle session est créée par WebDriver.
### Page Load Timeout: Spécifie l'intervalle de temps dans lequel la page Web doit être chargée dans un contexte de navigation actuel. Le délai d'expiration par défaut de 300 000 est imposé lorsqu'une nouvelle session est créée par WebDriver. Si le chargement de la page limite un délai donné/par défaut, le script sera arrêté par TimeoutException
### Implicit Wait Timeout: Cela spécifie le temps d'attente de la stratégie de localisation d'élément implicite lors de la localisation des éléments. Le délai d'attente par défaut de 0 est imposé lorsqu'une nouvelle session est créée par WebDriver.

## User Prompt Handler
### Cela définit l'action à entreprendre 
### lorsqu'une `user-prompt` se présente.
### Ceci est défini par la capacité unhandledPromptBehavior et présente les états suivants
### 1. dismiss : Toutes les boîtes de dialogue simples rencontrées doivent être ignorées
### 2. accept : Tous les dialogues simples rencontrés doivent être acceptés
### 3. dismiss and notify : Toutes les boîtes de dialogue simples rencontrées doivent être ignorées et une erreur doit être renvoyée indiquant que la boîte de dialogue a été traitée.
### 4. accept and notify : Toutes les boîtes de dialogue simples rencontrées doivent être acceptées et une erreur doit être renvoyée indiquant que la boîte de dialogue a été traitée.
### 5. ignore : toutes les boîtes de dialogue simples rencontrées doivent être laissées à l'utilisateur pour être gérées

## Headless : si on veut desactiver l'ouverture du navigateur (in background)     

## incognito : naviger en mode incognito

## user-agent: changer le nom de la machine/navigateur

## bot detection:
### La détection des robots Selenium fonctionne principalement en testant les variables JavaScript
### qui apparaissent lors de l'exécution de Selenium.
### Les détecteurs de robots vérifient souvent les mots « Selenium » ou « WebDriver » dans l'une des variables (sur l'objet fenêtre), ainsi que dans les variables de document nommées $cdc_ et $wdc_
### Ils vérifient également les valeurs des indicateurs d'automatisation dans le WebDriver,
### comme useAutomationExtension et navigator.webdriver.
### Ces attributs sont activés par défaut pour permettre une meilleure expérience de test et comme fonction de sécurité.
### pour plus de details : "https://www.zenrows.com/blog/selenium-avoid-bot-detection#disable-automation-indicator-webdriver-flags"


def test_page_load_strategy_timeouts(
    url: str, ## l'url du site web
    strategy: str, ## loading strategy
    promot_behv: str, ## le comportement du navigateur avec les prompts
    headless: bool = False, ## naviguer en mode headless
    incognito: bool =False ## naviguer en mode incognito
):
    
    # init options
    options = webdriver.ChromeOptions()
    
    # tester si le navigateur est chrome
    assert options.capabilities['browserName'] == 'chrome' , "votre navigateur n'est pas Chrome"

    # init le load strategy
    options.page_load_strategy = strategy
    
    # init timeouts
    options.timeouts = {
        'script': 5000,
        'pageLoad': 5000,
        'implicit': 5000
    }

    # prompts
    options.unhandled_prompt_behavior = promot_behv

    # changer user-agent
    user_agent = UserAgent()
    options.add_argument(f'user-agent={user_agent.random}')

    # activater headless mode (Sans GUI)
    if headless:
        options.add_argument("--headless") 

    # naviguer en mode incognito
    if incognito:
        options.add_argument("--incognito") 

    # pour empecher que le WebDriver piloté par Selenium soit détecté
    options.add_argument('--disable-blink-features=AutomationControlled') 

    # init driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # visiter un site web
    driver.get(url)
    driver.quit()

if __name__ == "__main__":
    
    # init options
    strategy = "normal" ## "eager" , "none"
    promot_behv = "accept", ## "dismiss", "dismiss and notify", "accept and notify", "ignore"
    headless = False ## naviguer en mode headless
    incognito = False ## naviguer en mode incognito

    # init url
    url = "https://www.selenium.dev/selenium/web/web-form.html" #"https://the-internet.herokuapp.com/javascript_alerts"

    # lancer le script
    test_page_load_strategy_timeouts(
        url=url,
        strategy=strategy,
        promot_behv=promot_behv,
        headless=headless,
        incognito=incognito,
    )