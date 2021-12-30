import scrapy
from ajar.items import AmazonUs,SpecsExtractor,ImageExtractor,SpecImage
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
# import numpy as np
import json
import requests
import pymongo
import urllib
from pandas import json_normalize
options = webdriver.FirefoxOptions()
	
	# enable trace level for debugging 
# options.log.level = "trace"
# fp = webdriver.FirefoxProfile()
# options.add_argument("--remote-debugging-port=9224")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
# options.add_argument("--window-size=1920,1080")
# binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))
binary = FirefoxBinary("/app/vendor/firefox/firefox")


class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "amazon_specs_data"
    rotate_user_agent = True
    allowed_domains = ["www.amazon.in"]
    # start_urls = [] 
    def start_requests(self):
        myclient = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@links-shard-00-00.rjots.mongodb.net:27017,links-shard-00-01.rjots.mongodb.net:27017,links-shard-00-02.rjots.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-xypyrq-shard-0&authSource=admin&retryWrites=true&w=majority")
        mydb = myclient.LinksDB
        mycol = mydb.Links
        mydoc = mycol.find({"store_id": 1})
        df = json_normalize(mydoc)
      
        for index, row in df.iterrows():
            sleep(1)
            print(index)
            yield scrapy.Request(row["product_id"], self.parse)
    def parse(self, response):
        browser = webdriver.Firefox(firefox_options=options,firefox_binary=binary,executable_path=os.environ.get('GECKODRIVER_PATH'))
        browser.get(response.url)
        scrapy_selector = Selector(text=browser.page_source)
        for i in scrapy_selector.css("#productDetails_techSpec_section_1 > tbody > tr") or scrapy_selector.css("#detailBullets_feature_div > ul > li"):
            pid = response.url
            specKey = i.css("th::text").get() or i.css("span > span.a-text-bold::text").get()
            specValue = i.css("td::text").get() or i.css("span > span:nth-child(2)::text").get()
            yield SpecsExtractor(pid=pid,specKey=specKey,specValue=specValue)       
        browser.close()
      
