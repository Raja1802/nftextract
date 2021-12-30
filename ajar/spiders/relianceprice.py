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
import pandas as pd
# import numpy as np
import json
import requests
import pymongo
import urllib
from pandas import json_normalize
from webdriver_manager.chrome import ChromeDriverManager
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "reliance_price_data"
    rotate_user_agent = True
    allowed_domains = ["www.reliancedigital.in"]
    # def __init__(self, arg1="", **kwargs):  # py36
        # super(QuotesInfiniteScrollSpider, self).__init__(**kwargs)  # python3
        # self.start_urls = [arg1]
    start_urls = []
    # def start_requests(self):
    #     myclient = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@links-shard-00-00.rjots.mongodb.net:27017,links-shard-00-01.rjots.mongodb.net:27017,links-shard-00-02.rjots.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-xypyrq-shard-0&authSource=admin&retryWrites=true&w=majority")
    #     mydb = myclient.LinksDB
    #     mycol = mydb.Links
    #     mydoc = mycol.find({"store_id": 33236})
    #     df = json_normalize(mydoc)
      
    #     urls = []
    #     for index, row in df.iterrows():
    #         urls.append(row["product_id"])
    #     df = 0 
    #     mycol = 0
    #     mydoc = 0
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        browser = webdriver.Chrome(
            # executable_path=ChromeDriverManager().install(),
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        # browser = webdriver.PhantomJS()
        browser.get(response.url)
        # sleep(3)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        
        pid = response.url
        price_mrp = scrapy_selector.css("#root > main > main > div.pb__20 > section.pdpStickyContainer > div.blk__sm__7.pdp__topBlock > div > div > div.pdp__priceSection > ul > li > span.pdp__mrpPrice::text").getall() or scrapy_selector.css("span.pdp__offerPrice::text").get()
        price = scrapy_selector.css("span.pdp__offerPrice::text").get() or scrapy_selector.css("span.pdp__offerPrice::text").get()
        price_2 = scrapy_selector.css("#root > main > main > div.pb__20 > section.pdpStickyContainer > div.blk__sm__7.pdp__topBlock > div:nth-child(5) > div:nth-child(2) > div.pdp__priceSection > ul > li.pdp__priceSection__priceListText.pdp__savePrice::text").getall() or scrapy_selector.css("li.pdp__savePrice::text").getall()
        yield PriceExtractor(pid=pid,price_mrp=price_mrp,price=price,price_2=price_2)

        # browser.close()
        browser.quit()
