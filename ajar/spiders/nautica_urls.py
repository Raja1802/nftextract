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
from fake_useragent import UserAgent
ua = UserAgent()
# # chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.binary_location = GOOGLE_CHROME_PATH



class QuotesSpider(SitemapSpider):

    name = "nautica_urls"
    rotate_user_agent = True
    allowed_domains = ["www.nautica.com"]
    # start_urls = ["https://www.nautica.com/"]

    # rules = (Rule(sle(allow="",), callback="parse_images",follow=True,),)

    sitemap_urls = [
        "https://www.nautica.com/sitemap_1.xml"
    ]

    def parse(self, response):
        UrlExtract = []
        UrlExtract = UrlExtracters()
     
        UrlExtract["url"] = response.url
        UrlExtract["canonical"] = response.css("head > link[rel='canonical']::attr(href)").get()
        UrlExtract["website"] =  "www.nautica.com"
        return UrlExtract