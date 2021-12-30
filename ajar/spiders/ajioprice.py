import scrapy
from ajar.items import AmazonUs,SpecsExtractor,ImageExtractor,SpecImage, PriceExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
ua = UserAgent()
import pandas as pd
# import numpy as np
import json
import requests
import pymongo
import urllib

from pandas import json_normalize
PROXY = "socks5://localhost:9051"
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH
from webdriver_manager.chrome import ChromeDriverManager

class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "ajio_price_data"
    rotate_user_agent = True
    allowed_domains = ["www.ajio.com"]
    # def __init__(self, arg1="", **kwargs):  # py36
    #     super(QuotesInfiniteScrollSpider, self).__init__(**kwargs)  # python3
    #     self.start_urls = [arg1]
    start_urls = []
    def parse(self, response):
      
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            # executable_path=ChromeDriverManager().install(),
            # executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_options,
        )
        # browser = webdriver.PhantomJS()
        browser.get(response.url)
        # sleep(0.5)
        # sleep(1)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        pid = response.url
        price_mrp =  scrapy_selector.css("div.prod-price-section > div.prod-price-sec > span.prod-cp::text").getall()
        price = scrapy_selector.css("div.prod-price-section > div.prod-sp::text").getall()
        price_2 =  scrapy_selector.css("div.prod-price-section > div.prod-price-sec > span.prod-discnt::text").getall()
        yield PriceExtractor(pid=pid,price_mrp=price_mrp,price=price,price_2=price_2)
            # return SpecsExtractor
        # for j in scrapy_selector.css("div._20Gt85"):
        #     ImageExtractor["image"] = j.css["div.q6DClP"].get()
        # yield SpecImage(images=ImageExtractor, specs=SpecsExtractor)
        browser.quit()
        # return amazon


# git push change usage comments
# push 1
