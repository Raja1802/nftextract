#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
from ajar.items import AmazonUs
from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# chrome requirments
# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
# chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesSpider(SitemapSpider):

    name = "localtest"
    rotate_user_agent = True
    allowed_domains = ["us.boohoo.com"]
    sitemap_urls = ["https://us.boohoo.com/sitemap_0-product.xml"]

    def parse(self, response):
        amazon = []
        amazon = AmazonUs()
        browser = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(0.5)
        scrapy_selector = Selector(text=browser.page_source)

        amazon["product_id"] = response.url
        amazon["product_mrp"] = scrapy_selector.css(
            "span.price-standard::text"
        ).getall()
        amazon["product_name"] = scrapy_selector.css(
            "h1.product-name::text"
        ).extract()
        amazon["product_description"] = scrapy_selector.css(
            "li.product-short-description-tab >div > p::text"
        ).getall()
        amazon["product_ASIN"] = scrapy_selector.css(
            'head >  meta[property="og:url"]::attr(content)'
        ).get()
        amazon["product_by_url"] = "boohoo.com"
        amazon["product_by_name"] = "boohoo"
        amazon["product_rating"] = (
            scrapy_selector.css(
                "div.productNo-bvStars >  div.bv-off-screen::text"
            ).getall()
            or "NULL"
        )
        amazon["product_image"] = (
            scrapy_selector.css(
                "#product-main-zoom::attr(href)"
            ).get()
            or scrapy_selector.css(
                "head > meta[property='og:image']::attr(content)"
            ).get()
        )
        amazon["product_price"] = scrapy_selector.css(
            "#product-content > div.product-price > span.price-sales::text"
        ).getall()
        amazon["product_price_2"] = scrapy_selector.css(
            "#product-content > div.product-price > span.price-sales > span::text"
        ).getall()
        amazon["product_about"] = scrapy_selector.css(
            "li.product-custom-composition-tab > div::text"
        ).getall()
        amazon["product_keywords"] = scrapy_selector.css(
            "#product-content > div.product-variations.js-product-variations > div.attribute.color-attribute > div.label.regular-product > span.selected-value::text"
        ).getall()
        amazon["product_catlog"] = scrapy_selector.css(
            "span.breadcrumb-element-name::text"
        ).getall()
        amazon["product_keywords_2"] = scrapy_selector.css(
            "head > meta[property='og:description']::attr(content)"
        ).getall()
        browser.quit()

        return amazon
