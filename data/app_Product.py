from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import sqlite3
import random
con = sqlite3.connect("entrance.db")
curses = con.cursor()


options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
browser.get("https://sportpoint.ru/catalog/?PAGEN_1=1")
time.sleep(3)
pages = []


for i in range(2, 378):
    pages.append(f"https://sportpoint.ru/catalog/?PAGEN_1={i}")

for page in pages:
    browser.get(page)
    time.sleep(3)

    name = browser.find_elements(By.CLASS_NAME, 'products-product__name')
    prices = browser.find_elements(By.CLASS_NAME, 'products-product-prices__price')
    for name_all, price_all in zip(name, prices):
        price_text = price_all.text.replace(")", "").replace(" ", "")
        type_name = name_all.text.split(' ',1,)
        manuf_er = type_name[1].split(' ',1)
        artikul = random.randint(999, 1000000)
        size = random.randint(36, 46)
        print(price_text,type_name[0],"-",manuf_er[0],artikul,size)
        try:
            curses.execute("INSERT INTO Product (Product_Сode, Product, Price,Size,Manufacturer,Photo) VALUES(?,?,?,?,?,?)", (artikul, type_name[0], int(price_text), size, manuf_er[0], "Photo\1.png"))
            con.commit()
        except sqlite3.IntegrityError:
            artikul = random.randint(999, 1000000)




con.close()