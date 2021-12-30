# runs in oracle cloud
# 
from time import sleep
import random
from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
# from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
# req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
# proxies = req_proxy.get_proxy_list() #this will create proxy list
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from fake_useragent import UserAgent
import os
delay = 0
ua = UserAgent()
opts = FirefoxOptions()
opts.add_argument("--headless")

def some_job():
    for i in range(0, 200000):
        userAgent = ua.random
        profile = webdriver.FirefoxProfile()
        print(userAgent)
        PROXY = "socks5://localhost:9050"
        proxy_ip = "localhost"
        proxt_port = "9050"
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference( "network.proxy.socks_version", 5 )
        profile.set_preference("network.proxy.socks", str(proxy_ip))
        profile.set_preference("network.proxy.socks_port", int(proxt_port))
        profile.set_preference( "network.proxy.socks_remote_dns", True )
        profile.set_preference("general.useragent.override", userAgent)
        profile.update_preferences()
        driver = webdriver.Firefox(executable_path='geckodriver',options=opts,firefox_profile=profile)
        episode_id = random.randint(126871, 253992)
        url = f"https://ajarani.me/episode/{episode_id}"
        try:
            driver.get(url=url)
        except:
            driver.get(url="https://ajarani.me/explore")
        # time_1 = random.randint(3,5)
        # sleep(time_1)
        # try:
        #     # resultSet = driver.find_element_by_class_name("exo-native-widget-outer-container")
        #     # options = resultSet.find_element_by_class_name("exo-native-widget-item")
        #     # for option in options:
        #     #     option.click()
        #     #     sleep(5)
        #     element = browser.find_element_by_xpath('//*[@id="exoNativeWidget4042496"]/div[2]/div[2]/a')
        #     element.click()
        #     time_2 = random.randint(4,6)
        #     sleep(time_2)
        #     print("clicked")
        # except: 
        #     print("no <a> tag! maybe page not loaded fully")
        # time_3 = random.randint(3,5)    
        # sleep(time_3)
        print("success")
        driver.quit()
for i in range(0, 200000):
    userAgent = ua.random
    profile = webdriver.FirefoxProfile()
    print(userAgent)
    PROXY = "socks5://localhost:9050"
    proxy_ip = "localhost"
    proxt_port = "9050"
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference( "network.proxy.socks_version", 5 )
    profile.set_preference("network.proxy.socks", str(proxy_ip))
    profile.set_preference("network.proxy.socks_port", int(proxt_port))
    profile.set_preference( "network.proxy.socks_remote_dns", True )
    profile.set_preference("general.useragent.override", userAgent)
    profile.update_preferences()
    driver = webdriver.Firefox(options=opts,firefox_profile=profile)
    episode_id = random.randint(126871, 253992)
    url = f"https://ajarani.me/episode/{episode_id}"
    try:
        driver.get(url=url)
    except:
        driver.get(url="https://ajarani.me/explore")     
    # driver.get(url=url)
    # time_1 = random.randint(2,7)
    # sleep(time_1)
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
    # time_3 = random.randint(3,5)    
    # sleep(time_3)
    driver.quit()
scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', hours=1)
scheduler.start()