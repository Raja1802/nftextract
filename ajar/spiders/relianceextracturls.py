import scrapy
from ajar.items import AmazonUs, UrlExtracters
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "rlcdig_url"
    rotate_user_agent = True
    allowed_domains = ["www.reliancedigital.in"]
    start_urls = ["https://www.reliancedigital.in/"]
    rules = (Rule(sle(allow="/p/",deny=("/c/", )), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse_result(self, response):
        UrlExtract = []
        UrlExtract = UrlExtracters()
        scrapy_selector = response
        UrlExtract["url"] = response.url
        UrlExtract["canonical"] = response.css("head > link[rel='canonical']::attr(href)").get()
        UrlExtract["website"] =  "www.reliancedigital.in"
        return UrlExtract
