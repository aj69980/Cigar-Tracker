import requests
from bs4 import BeautifulSoup as bs
import datetime as dt
import time as t
import random
import pandas
import csv
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

# Collect Current Date
current_date = dt.date.today()
current_date = (str(current_date))
# print(current_date)

# # Choose Which Cigar to Check
# print("which Cigar are you tracking?")
# print("1: Arturo Fuente Hemingway Short Story \n" + "2: Arturo Fuente Hemingway Best Seller")
# which_cigar = input()

# if which_cigar == "1":
#     god_url = "https://cigargod.com/collections/hemingway/products/arturo-fuente-hemingway-short-story"
# if which_cigar == "2":
#     god_url = "https://cigargod.com/collections/hemingway/products/arturo-fuente-hemingway-best-seller"
# # print(god_url)

# god_html = requests.get(god_url).text

# god_soup = bs(god_html, "lxml")
# god_title = god_soup.find("h1", class_="product-single__title").text
# god_price = god_soup.find("span", class_ = "product-single__price").text.replace(" ", "")
# print(god_title,god_price)

options = ChromeOptions()
options.headless=True
browser = webdriver.Chrome(options=options)
fox_url = "https://foxcigar.com/shop/cigars/arturo-fuente/hemingway/short-story/"
# browser.get(fox_url)

fox_title = []
def fox_info():
    try:
        browser.get(fox_url)
        t.sleep(3)
        
        # Get Title
        title = browser.title
        fox_title.append(title)
        
        
        # Close Popup
        browser.find_element(By.XPATH, "/html/body/div[9]/div/div/div/div/div/div/button").click()
        t.sleep(random.randrange(1,2))



        # Dropdown Clicker
        dropbox = browser.find_element(By.ID, "pa_cigar-count")
        drp = Select(dropbox)
        drp.select_by_visible_text("Single")
        t.sleep(random.randrange(5))

        # Pulls Price
        price = browser.find_element(By.CSS_SELECTOR, "#product-47749 > div:nth-child(1) > div > div > div > div.col-sm-6.summary.entry-summary > div > div > form > div > div.woocommerce-variation.single_variation > div.woocommerce-variation-price > span > span > bdi")
        price=price.text
        return (price)
        
        browser.close()  
        
    except Exception as err:
        print(err)
        browser.quit()

price = fox_info()

fox_title = str(fox_title[0])
fox_title = fox_title[0:((fox_title.index("Story"))+5)] 
print(fox_title)
print(price)