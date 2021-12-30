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
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesSpider(SitemapSpider):

    name = "adidas"
    rotate_user_agent = True
    allowed_domains = ["www.adidas.com"]
    # start_urls = ["https://www2.hm.com/"]

    # rules = (Rule(sle(allow="en_us",), callback="parse_images", follow=True,),)

    sitemap_urls = [
        "https://www.adidas.com/on/demandware.static/-/Sites-CustomerFileStore/default/adidas-US/en_US/sitemaps/product/adidas-US-en-us-product.xml"
    ]

    def parse(self, response):
        amazon = []
        amazon = AmazonUs()
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(0.1)
        scrapy_selector = Selector(text=browser.page_source)

        amazon["product_id"] = response.url
        amazon["product_mrp"] = scrapy_selector.css(
            "span.gl-price__value.gl-price__value--crossed::text"
        ).get()
        amazon["product_name"] = scrapy_selector.css(
            "h1[data-auto-id='product-title']::text"
        ).get()
        amazon["product_description"] = scrapy_selector.css(
            "div#navigation-target-description > div > div > p::text"
        ).getall()
        amazon["product_ASIN"] = scrapy_selector.css(
            'head >  meta[property="og:url"]::attr(content)'
        ).get()
        amazon["product_by_url"] = "adidas.com"
        amazon["product_by_name"] = "adidas"
        amazon["product_rating"] = (
            scrapy_selector.css(
                "div.productNo-bvStars >  div.bv-off-screen::text"
            ).getall()
            or "NULL"
        )
        amazon["product_image"] = (
            scrapy_selector.css("head > meta[property='og:image']::attr(content)").get()
            or scrapy_selector.css(
                "#navigation-target-gallery > section > div > div> div > img::attr(src)"
            ).get()
        )
        amazon["product_price"] = scrapy_selector.css(
            "span.gl-price__value.gl-price__value--sale::text"
        ).get()
        amazon["product_price_2"] = scrapy_selector.css(
            "span.gl-price__value.gl-price__value--sale::text"
        ).getall()
        amazon["product_about"] = scrapy_selector.css(
            "div#navigation-target-specifications > div> div> ul > li::text"
        ).getall()
        amazon["product_keywords"] = scrapy_selector.css(
            "#app > div > div > div > div > div.content-wrapper___3AhOy > div.sidebar-wrapper___26z7B > div.sidebar___2C-EP > div > div.color-and-price___2q0A2 > h5::text"
        ).getall()
        amazon["product_catlog"] = scrapy_selector.css(
            "#app > div > div > div > div > div.content-wrapper___3AhOy > div.content___1rB-s > div > div.gallery-section___tEM20 > ol > li > a > span::text"
        ).getall()
        amazon["product_keywords_2"] = scrapy_selector.css(
            "head > meta[property='og:description']::attr(content)"
        ).getall()
        browser.quit()

        return amazon
