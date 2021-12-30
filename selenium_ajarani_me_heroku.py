# runs in oracle cloud
from time import sleep
import random
# from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from fake_useragent import UserAgent
import os
import json
delay = 0
import pymongo
import urllib
ua = UserAgent()
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
m=0
client = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@cluster0-shard-00-00.1vax0.mongodb.net:27017,cluster0-shard-00-01.1vax0.mongodb.net:27017,cluster0-shard-00-02.1vax0.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-umkr09-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.nft
collect = db["gimmiproxy"]
def some_job():
    for i in range(0, 200000):
        userAgent = ua.random
        print(userAgent)
        prox = list(collect.aggregate([{'$sample': {'size': 1 }}]))
        PROXY = str(prox[0]["proxy"]["curl"])
        # PROXY = "socks5://127.0.0.1:9050"
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument(f'user-agent={userAgent}')
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options,)
        episode_id = random.randint(126871, 253992)
        url = f"https://amuseanime.netlify.app/episode/{episode_id}"
        # url = f"https://ouo.io/9IxejF"
        try:
            response = driver.get(url=url)
            sleep(20)
            # print(response)
        except:
            driver.get(url="https://amuseanime.netlify.app/episode/126871")
            sleep(20)
        # ran = 8
        # if(m%ran == 0):
        #     time_1 = random.randint(3,5)
        #     sleep(time_1)
        #     try:
        #         sleep(5)
        #         ran_frame = random.randint(4,6)
        #         driver.switch_to.frame(ran_frame)
        #         sleep(2)
        #         options = driver.find_element_by_tag_name('a')
        #         options.click()
        #         sleep(6)
        #         print("clicked")
        #     except: 
        #         print("no <a> tag! maybe page not loaded fully")
        m = m+1
        sleep(3)
        print("success")
        driver.quit()
for i in range(0, 200000):
    userAgent = ua.random
    print(userAgent)
    prox = list(collect.aggregate([{'$sample': {'size': 1 }}]))
    PROXY = str(prox[0]["proxy"]["curl"])
    # PROXY = "socks5://127.0.0.1:9050"
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options,)
    episode_id = random.randint(126871, 253992)
    url = f"https://amuseanime.netlify.app/episode/{episode_id}"
    # url = f"https://ouo.io/9IxejF"
    try:
        response = driver.get(url=url)
        # print(response)
        sleep(20)
    except:
        driver.get(url="https://amuseanime.netlify.app/episode/126871")  
        sleep(20)
    # ran = 8
    # if(m%ran == 0):
    #     time_1 = random.randint(3,5)
    #     sleep(time_1)
    #     try:
    #         sleep(3)
    #         ran_frame = random.randint(4,6)
    #         driver.switch_to.frame(ran_frame)
    #         sleep(2)
    #         options = driver.find_element_by_tag_name('a')
    #         options.click()
    #         sleep(6)
    #         print("clicked")
    #     except: 
    #         print("no <a> tag! maybe page not loaded fully")
    m = m+1
    sleep(3)
    driver.quit()
# scheduler = BlockingScheduler()
# scheduler.add_job(some_job, 'interval', hours=1)
# scheduler.start()

# asaklajskajskl