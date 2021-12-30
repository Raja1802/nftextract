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
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH

# options = webdriver.FirefoxOptions()
	
# 	# enable trace level for debugging 
# # options.log.level = "trace"
# # fp = webdriver.FirefoxProfile()
# # options.add_argument("--remote-debugging-port=9224")
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# # options.add_argument("--window-size=1920,1080")
# # binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))
# binary = FirefoxBinary("/app/vendor/firefox/firefox")



class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "reliance_specs_data"
    rotate_user_agent = True
    allowed_domains = ["www.reliancedigital.in"]
    start_urls = []
    # def start_requests(self):
    #     myclient = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@links-shard-00-00.rjots.mongodb.net:27017,links-shard-00-01.rjots.mongodb.net:27017,links-shard-00-02.rjots.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-xypyrq-shard-0&authSource=admin&retryWrites=true&w=majority")
    #     mydb = myclient.LinksDB
    #     mycol = mydb.Links
    #     mydoc = mycol.find({"store_id": 33236})
    #     df = json_normalize(mydoc)
    #     # columns = ['product_id']
    #     # for column in columns:
    #     #     df[column] = df[column].astype(str)
    #     #     df[column] =  "https://www.flipkart.com" + df[column]
    #     # df.drop(df[df["url"] == "https://www.flipkart.comNAN"].index, inplace=True)
    #     # df = pd.read_csv(r"C:\Users\G RAJA\Desktop\ajarani.me\data\exports\AnimeApi\daily\converted_csv\07-02-2021.csv")
    #     # df2 = df.drop_duplicates(subset="ep_url" , keep='first')
    #     # df2 = df2.iloc[60000:]
    #     urls = []
    #     for index, row in df.iterrows():
    #         print(index)
    #         sleep(1)
    #         yield scrapy.Request(url=row["product_id"], callback=self.parse)
           
    # rules = (Rule(sle(allow=( "shirt", "shoes","mobile","cycle","women","men","/p/"), deny=("product-reviews")), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse(self, response):
       
        # browser = webdriver.Firefox(firefox_options=options,firefox_binary=binary,executable_path=os.environ.get('GECKODRIVER_PATH'))
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
        browser.get(response.url)
        # sleep(0.5)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        for i in scrapy_selector.css("#pdp__specification > section > ul.pdp__tab-info__list"):
            pid = response.url
            specKey = i.css("div.pdp__tab-info__list__name::text").get()
            specValue = i.css("div.pdp__tab-info__list__value::text").get()
            yield SpecsExtractor(pid=pid,specKey=specKey,specValue=specValue)
            
        browser.quit()
        