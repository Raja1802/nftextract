from time import sleep
import schedule 
import random
import pymongo
import urllib
from apscheduler.schedulers.blocking import BlockingScheduler
# from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
# req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
# proxies = req_proxy.get_proxy_list() #this will create proxy list
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
# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
# CHROMEDRIVER_PATH = "./chromedriver"

# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
# CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = GOOGLE_CHROME_PATH
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# client = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@cluster0-shard-00-00.1vax0.mongodb.net:27017,cluster0-shard-00-01.1vax0.mongodb.net:27017,cluster0-shard-00-02.1vax0.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-umkr09-shard-0&authSource=admin&retryWrites=true&w=majority")
# db = client.nft
# collect = db["gimmiproxy"]
delay = 3
ua = UserAgent()
def some_job():
    print("called for job")
    for i in range(1, 27000):
        print(i)
        userAgent = ua.random
        print(userAgent)
        chrome_options.add_argument(f'user-agent={userAgent}')
        # prox = list(collect.aggregate([{'$sample': {'size': 1 }}]))
        # PROXY = str(prox[0]["proxy"]["curl"])
        response = s.get(url="https://gimmeproxy.com/api/getProxy")
        data = response.json()
        print(data)
        PROXY = str(data["curl"])
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--ignore-ssl-errors')
#         PROXY = "socks5://localhost:9150"
#         chrome_options.add_argument('--proxy-server=%s' % PROXY)
        browser = webdriver.Chrome(
                executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                chrome_options=chrome_options,
            )
        episode_id = random.randint(126871, 253992)
        url = f"https://amuseanime.netlify.app/episode/{episode_id}"  
        browser.get(url=url)
        time_1 = random.randint(5,7)
        sleep(time_1)
        try:
            # sleep(time_2)
            
            print("clicked")
            sleep(10)
            sleep(5)
            browser.save_screenshot('ss.png')
        except: 
            print("no <a> tag! maybe page not loaded fully")
        
        time_3 = random.randint(2,4)    
        sleep(time_3)

        print("success")
        browser.quit()
for i in range(2, 4):
    userAgent = ua.random
    print(userAgent)
    # chrome_options.add_argument(f'user-agent={userAgent}')
    # prox = list(collect.aggregate([{'$sample': {'size': 1 }}]))
    response = s.get(url="https://gimmeproxy.com/api/getProxy")
    data = response.json()
    print(data)
    PROXY = str(data["curl"])
    print(data["country"])
    # PROXY = str(prox[0]["proxy"]["curl"])
    # PROXY = "socks4://179.57.117.107:42630"
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)
#     PROXY = "socks5://localhost:9150"
#     chrome_options.add_argument('--proxy-server=%s' % PROXY)
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_options,
        )
    episode_id = random.randint(126871, 253992)
    # url = f"https://amuseanime.netlify.app/episode/{episode_id}"   
    url="https://gogoplay.io/download?id=MTMxNDk2&typesub=Gogoanime-DUB&title=Kimetsu+no+Yaiba+%28Dub%29+Episode+1"
    try:
        browser.get(url=url)
        time_1 = random.randint(5,7)
        sleep(time_1)
        sleep(20)
    except:
        print("failed")
    try:
        time_2 = random.randint(5,7)
        ran_frame = random.randint(1,10)
        # browser.switch_to.frame(ran_frame)
        sleep(2)
        options = browser.find_element_by_class_name("dowload")
        options.click()
        sleep(time_2)
        sleep(60)
        # browser.save_screenshot('ss.png')
        print("clicked")
    except: 
        try:
            time_2 = random.randint(5,7)
            ran_frame = random.randint(4,6)
            browser.switch_to.frame(ran_frame)
            sleep(2)
            options = browser.find_element_by_tag_name('a')
            options.click()
            sleep(time_2)
            sleep(60)
            print("clicked")
        except:
            print("failed everywhere")
        print("no <a> tag! maybe page not loaded fully")
    time_3 = random.randint(2,4)    
    sleep(time_3)
    print("success")
    browser.quit()
schedule.every(1).minutes.do(some_job) 
while True: 
    schedule.run_pending() 
    sleep(1)
