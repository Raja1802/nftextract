import scrapy
from ajar.items import AmazonUs,SpecsExtractor,ImageExtractor,SpecImage
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


class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "puma_images_data"
    rotate_user_agent = True
    # allowed_domains = ["www.flipkart.com"]
    start_urls = []
    def parse(self, response):
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        scrapy_selector = Selector(text=browser.page_source)
        for i in scrapy_selector.css("div.glide-slide"):
            pid = response.url
            image = i.css("img::attr(data-src)").get()
            yield ImageExtractor(pid=pid,image=image)
        # browser.quit()
     