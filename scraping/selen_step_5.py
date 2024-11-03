from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time

def scroll(url, driver):
    
    driver.get(url)
    time.sleep(5)

    i = 0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #driver.execute_script("window.scrollTo(0, 1000)")

        time.sleep(5)
        if i == 2:
            break
        i=i+1


def test_scroll_to_element(url,driver):
    
    # visiter un site web
    driver.get(url)
    time.sleep(5)

    # localiser le iframe
    iframe = driver.find_element(By.TAG_NAME, "iframe")

    # lancer le scrolling
    ActionChains(driver)\
        .scroll_to_element(iframe)\
        .perform()

    time.sleep(4)
    driver.quit()

if __name__ == "__main__":
    
    # init url
    url = "https://www.selenium.dev/selenium/web/scrolling_tests/frame_with_nested_scrolling_frame_out_of_view.html"

    # init driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
    )

    # lancer le script
    #test_scroll_to_element(url=url, driver=driver)
    scroll(url=url, driver=driver)