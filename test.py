from selenium import webdriver
import os
from fake_useragent import UserAgent
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing.pool import ThreadPool
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxOptions 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json 
opts = FirefoxOptions()
# opts.add_argument("--headless")
ua = UserAgent()
# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
# CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
chrome_options = Options()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
PROXY = "socks5://localhost:9150"
# PROXY = "socks4://192.111.139.162:4145"
userAgent = ua.random
print(userAgent)
# profile = webdriver.FirefoxProfile()
# proxy_ip = "localhost"
# proxt_port = "9050"
# profile.set_preference("network.proxy.type", 1)
# profile.set_preference( "network.proxy.socks_version", 5 )
# profile.set_preference("network.proxy.socks", str(proxy_ip))
# profile.set_preference("network.proxy.socks_port", int(proxt_port))
# profile.set_preference( "network.proxy.socks_remote_dns", True )

# profile.set_preference("general.useragent.override", userAgent)
# profile.update_preferences()
# opts.add_argument(f'user-agent={userAgent}')
# opts.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument(f'user-agent={userAgent}')
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options,)
# driver.get(url="https://gimmeproxy.com/api/getProxy")
# sleep(3)
# pre = driver.find_element_by_tag_name("pre").text
# data = json.loads(pre)
# print(data["curl"])
# PROX = str(data["curl"])
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options,)
browser.get(url="https://ajarmailer.ga/episode/136334/")
sleep(10)
browser.switch_to.frame(6)
# browser.find_element_by_xpath('//*[@id="container-c9f5aa15daaa4cd496946eda31691663"]/div[2]/div[1]/div/a')
sleep(5)
options = browser.find_element_by_tag_name('a')
# resultSet_a = driver.find_element_by_class_name("exo-native-widget-outer-container")
# browser.find_elements_by_id("container-c9f5aa15daaa4cd496946eda31691663")
sleep(2)
# options = browser.find_element_by_xpath('//*[@id="container-c9f5aa15daaa4cd496946eda31691663"]/div[2]/div[1]/div/a')
# resultSet_a = driver.find_element_by_class_name("exo-native-widget-item-container")
# options = resultSet_a.find_element_by_class_name("exo-native-widget-item")
        
# options = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))
# driver.execute_script("arguments[0].click();", options)
options.click()
print("clicked")
sleep(1)
# for option in options:
#     option.click()
#     sleep(5)
# print(resultSet)
# driver.quit()
browser.quit()
# zipit
# https://gimmeproxy.com/api/getProxy for proxies 
def web_scraper(x):
    latitiude = 42.1408845
    longitude = -72.5033907
    accuracy = 100
    
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options,)
    browser.execute_cdp_cmd(
        "Browser.grantPermissions",
        {
            "origin": "https://www.openstreetmap.org/",
            "permissions": ["geolocation"]
        },
    )
    browser.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": 35.689487,
            "longitude": 139.691706,
            "accuracy": 100,
        },
    )
    browser.get(url="https://ajarani.me/")
    sleep(2)
    print(x)
    browser.quit()

if __name__ == "__main__":
    p = ThreadPool(15)
    pool_output = p.map(web_scraper, range(30))