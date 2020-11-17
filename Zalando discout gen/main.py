from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bs4
from config import Settings as s
import time
import names
import random

def discount():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get("https://www.zalando."s['country]"/zalando-newsletter/")
    time.sleep(1.5)
    driver.find_element_by_id("uc-btn-accept-banner").click()
    time.sleep(1)

    driver.find_element_by_xpath("//div[2]/label").click()

    namefirst = names.get_first_name()
    namelast = names.get_last_name()
    mail = str(random.randint(0,9)) + namefirst + namelast + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + "@" + s['catchall']

    r = driver.page_source
    soup = bs4.BeautifulSoup(r, "lxml")
    for i in soup.find_all("form", class_="subscription__form"):
        for i2 in i.find_all("input"):
            i2 = i2["id"]
        for i3 in i.find_all("button"):
            i3 = i3["class"]

    time.sleep(0.5)
    driver.find_element_by_id(i2).send_keys(mail)
    time.sleep(0.5)

    driver.find_element_by_xpath('//form/button/span').click()
    time.sleep(2)
    driver.close()

for i in range(s['ammount']):
    discount()
    print(str(i+1)+ ". Succesfuly generated discount code please check mail")
