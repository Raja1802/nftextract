from time import sleep
import schedule 
import random
import pymongo
import urllib
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from fake_useragent import UserAgent
import os
import requests
s = requests.Session()
CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"C:\Users\G RAJA\Desktop\ajarani.me\ipfs"}
chrome_options.add_experimental_option("prefs",prefs)
# chrome_options.binary_location = GOOGLE_CHROME_PATH
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
client = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@cluster0-shard-00-00.1vax0.mongodb.net:27017,cluster0-shard-00-01.1vax0.mongodb.net:27017,cluster0-shard-00-02.1vax0.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-umkr09-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = client.anime
mycol = mydb["ggspider_dat"]
mydoc = mycol.find()
from pandas import json_normalize
df = json_normalize(mydoc)
df.shape
df.dropna(inplace=True)
delay = 3
ua = UserAgent()
df = df.head(5)


for index, rowe in df.iterrows():
    userAgent = ua.random
    print(userAgent)
    browser = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_options,
        )
    url=rowe["download_1"]
    try:
        browser.get(url=url)
        time_1 = random.randint(5,7)
        sleep(time_1)
        sleep(30)
    except:
        print("failed to load page")
    try:
        time_2 = random.randint(5,7)
        ran_frame = random.randint(1,10)
        sleep(2)
        options = browser.find_element_by_css_selector("#content-download > div:nth-child(1) > div:nth-child(6) > a")
        options.click()
        sleep(time_2)
        sleep(60)
        print("downloaded the video")
    except: 
       print("failed to download the video")
    print("success")
    browser.close()

