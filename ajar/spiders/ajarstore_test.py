#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
import requests
from ajar.items import AmazonUs
from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import time
import random
import csv
# chrome requirments
# GOOGLE_CHROME_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.binary_location = GOOGLE_CHROME_PATH
# ua = UserAgent()

class QuotesSpider(CrawlSpider):

    name = "ajartest"
    rotate_user_agent = True
    # url = "https://dist.torproject.org/torbrowser/10.0.2/tor-browser-linux64-10.0.2_en-US.tar.xz"
    # r = requests.get(url, allow_redirects=True)
    # open('tor-browser-linux64-10.0.2_en-US.tar.xz', 'wb').write(r.content)
    allowed_domains = ["ajarstore.com"]
    start_urls = ["https://ajarstore.com/"]

    rules = (Rule(sle(allow="",), callback="parse_images", follow=True,),)

    # sitemap_urls = [
    #     "https://www.adidas.com/on/demandware.static/-/Sites-CustomerFileStore/default/adidas-US/en_US/sitemaps/product/adidas-US-en-us-product.xml"
    # ]

    def parse_images(self, response):
        
        amazon = []
        amazon = AmazonUs()
        # userAgent = ua.chrome
        # print(userAgent)
        # chrome_options.add_argument(f'user-agent={userAgent}')
        browser = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        time.sleep(5)
        # element = browser.find_element_by_xpath("//*[@id='root']/main/div[2]/a")
        # element.click()
        # time.sleep(5)
        # print(browser.current_url) 
       
        scrapy_selector = Selector(text=browser.page_source)

        amazon["product_id"] = response.url
       
        browser.quit()

        return amazon


# import tbselenium.common as cm
# from tbselenium.tbdriver import TorBrowserDriver
# from tbselenium.utils import launch_tbb_tor_with_stem

# tbb_dir = r"tor-browser_en-US"
# tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_dir)
# with TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM) as driver:
#     driver.load_url("https://check.torproject.org")

# tor_process.kill()