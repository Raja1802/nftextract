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
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH
from webdriver_manager.chrome import ChromeDriverManager


class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "flipkart_price_data"
    rotate_user_agent = True
    allowed_domains = ["www.flipkart.com"]
    ## below code for scrapyd 
    # def __init__(self, arg1="", **kwargs):  # py36
    #     super(QuotesInfiniteScrollSpider, self).__init__(**kwargs)  # python3
    #     self.start_urls = [arg1]
    start_urls = []
    def parse(self, response):
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            # executable_path=ChromeDriverManager().install(),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        pid = response.url
        price_mrp = scrapy_selector.css("#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._3I9_wc._2p6lqe::text").getall() or scrapy_selector.css("div._3I9_wc._2p6lqe::text").getall()
        price = scrapy_selector.css("#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._30jeq3._16Jk6d::text").getall() or scrapy_selector.css("div._30jeq3._16Jk6d::text").getall()
        price_2 = scrapy_selector.css("#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._3Ay6Sb._31Dcoz > span::text").getall() or scrapy_selector.css("div._3Ay6Sb._31Dcoz > span::text").getall()
        yield PriceExtractor(pid=pid,price_mrp=price_mrp,price=price,price_2=price_2)
        browser.quit()
   