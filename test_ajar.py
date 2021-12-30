from time import sleep
import random
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
CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
delay = 3
ua = UserAgent()
def some_job():
    for i in range(2, 27000):
        userAgent = ua.random
        print(userAgent)
        chrome_options.add_argument(f'user-agent={userAgent}')
        PROXY = "socks5://localhost:9150"
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        browser = webdriver.Chrome(
                executable_path=CHROMEDRIVER_PATH,
                chrome_options=chrome_options,
            )
        url = f"https://ajarani.me/item/{i}"        
        browser.get(url=url)
        time_1 = random.randint(5,7)
        sleep(time_1)
        try:
            # resultSet = driver.find_element_by_class_name("exo-native-widget-outer-container")
            # options = resultSet.find_element_by_class_name("exo-native-widget-item")
            # for option in options:
            #     option.click()
            #     sleep(5)
            element = browser.find_element_by_xpath('//*[@id="exoNativeWidget4042496"]/div[2]/div[2]/a')
            element.click()
            time_2 = random.randint(4,6)
            sleep(time_2)
            print("clicked")
        except: 
            print("no <a> tag! maybe page not loaded fully")
        time_3 = random.randint(3,5)    
        sleep(time_3)
        print("success")
        browser.quit()
for i in range(126871, 253992):
    
    userAgent = ua.random
    print(userAgent)
    chrome_options.add_argument(f'user-agent={userAgent}')
    PROXY = "socks5://localhost:9150"
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_options,
        )
    
    url = f"https://ajarani.me/episode/{i}"        
    browser.get(url=url)
    time_1 = random.randint(5,7)
    sleep(time_1)
    # try:
        # resultSet = browser.find_element_by_class_name("exo-native-widget-outer-container")
        # options = resultSet.find_element_by_class_name("exo-native-widget-item")
        # for option in options:
        #     option.click()
        #     sleep(5)
        # element = browser.find_element_by_xpath('//*[@id="container-c5df4e3fd9c30eb6a6083deb83df6ebd"]/div[2]/div[2]/div/a')
        # element.click()
        # element = browser.find_element_by_xpath('//*[@id="container-c5df4e3fd9c30eb6a6083deb83df6ebd"]/div[2]/div[1]/div/a')
        # element.click()
        # element = browser.find_element_by_xpath('//*[@id="exoNativeWidget4042496"]/div[2]/div[1]/a')
        # element.click()
        # time_2 = random.randint(5,7)
        # sleep(time_2)
        # print("clicked")
        # myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'propads')))
        # element = browser.find_element_by_class_name("propads")
        # element.click()
        
    # except: 
    #     print("no <a> tag! maybe page not loaded fully")
    time_3 = random.randint(3,5)    
    sleep(time_3)
    browser.quit()
# scheduler = BlockingScheduler()
# scheduler.add_job(some_job, 'interval', hours=1)
# scheduler.start()