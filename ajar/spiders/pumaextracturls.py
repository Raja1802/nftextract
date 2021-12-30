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
    name = "pumain_url"
    rotate_user_agent = True
    allowed_domains = ["in.puma.com"]
    start_urls = ["https://in.puma.com/"]

    rules = (Rule(sle(allow="",), callback="parse_result", follow=True),)

    def parse_result(self, response):
        UrlExtract = []
        UrlExtract = UrlExtracters()
        scrapy_selector = response
        UrlExtract["url"] = response.url
        UrlExtract["canonical"] = response.css("head > link[rel='canonical']::attr(href)").get()
        UrlExtract["website"] =  "in.puma.com"
        return UrlExtract
