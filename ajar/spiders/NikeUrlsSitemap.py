
import scrapy
from ajar.items import AmazonUs, UrlExtracters
from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# # chrome requirments
# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
# CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesSpider(SitemapSpider):

    name = "nikeus"
    rotate_user_agent = True
    allowed_domains = ["www.nike.com"]
    # start_urls = ["https://www2.hm.com/"]

    # rules = (Rule(sle(allow="en_us",), callback="parse_images", follow=True,),)

    sitemap_urls = [
        "https://www.nike.com/sitemap-pdp-en-us.xml"
    ]

    def parse(self, response):
        UrlExtract = []
        UrlExtract = UrlExtracters()
        scrapy_selector = response
        UrlExtract["url"] = response.url
        UrlExtract["canonical"] = response.css("head > link[rel='canonical']::attr(href)").get()
        UrlExtract["website"] =  "www.nike.com"
        return UrlExtract