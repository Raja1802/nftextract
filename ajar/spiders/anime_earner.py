import scrapy
from ajar.items import AmazonUs,SpecsExtractor,ImageExtractor,SpecImage
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from os import getcwd
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
import json
import requests
import pymongo
import urllib
from pandas import json_normalize
from fake_useragent import UserAgent
ua = UserAgent()
s = requests.Session()

GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
from webdriver_manager.chrome import ChromeDriverManager



class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "anime_earner"
    rotate_user_agent = True
    allowed_domains = ["amuseanime.netlify.app"]
    start_urls = []
    def parse(self, response):
        # PROXY = "socks5://localhost:9050"
        respo = s.get(url="https://gimmeproxy.com/api/getProxy")
        data = respo.json()

        PROXY = str(data["curl"])
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        userAgent = ua.random
        chrome_options.add_argument(f'user-agent={userAgent}')
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        print(response.url)
        yo = browser.get(url=response.url)
        print(yo)
        sleep(15)         
        browser.quit()

#kajhs     ashk