from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time, random

browser = wd.Chrome("chromedriver")
reddit_url = "https://www.reddit.com/r/cigars/"


def search_reddit():
    try:
        browser.get(reddit_url)
        time.sleep(3)
        
        browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/button").click()
        time.sleep(5)
















    
    except Exception as err:
        browser.quit()    
        
search_reddit()