import scrapy
from ajar.items import AmazonUs
from scrapy.spiders import CrawlSpider, Rule
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
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "petsmart"
    rotate_user_agent = True
    allowed_domains = ["www.petsmart.com"]
    start_urls = ["https://www.petsmart.com/"]
    rules = (Rule(sle(allow="",), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse_result(self, response):
        amazon = []
        amazon = AmazonUs()
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(0.5)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags

        amazon["product_id"] = response.url
        amazon["product_mrp"] = scrapy_selector.css(
            "div.product-price > span > span.product-price-standard::text"
        ).getall()
        amazon["product_name"] = scrapy_selector.css(
            "div.product-header > div > div > h1::text"
        ).extract()
        amazon["product_description"] = scrapy_selector.css(
            "#react-tabs-1 > div > p:nth-child(2)::text"
        ).getall()
        amazon["product_ASIN"] = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "petsmart.com"
        amazon["product_by_name"] = "petsmart"
        amazon["product_rating"] = (
            scrapy_selector.css(
                "div.productNo-bvStars >  div.bv-off-screen::text"
            ).getall()
            or "NULL"
        )
        amazon["product_image"] = (
            scrapy_selector.css(
                "div.pdp-image-viewer > div > div.react-viewer-canvas > img::attr(src)"
            ).get()
            or scrapy_selector.css(
                "head > meta[property='og:image']::attr(content)"
            ).get()
        )
        amazon["product_price"] = scrapy_selector.css(
            "div.product-price > span > span.product-price-sales::text"
        ).getall()
        amazon["product_price_2"] = scrapy_selector.css(
            "div.product-price > span > span.product-price-sales::text"
        ).getall()
        amazon["product_about"] = scrapy_selector.css(
            "#react-tabs-3 > div > p::text"
        ).getall()
        amazon["product_keywords"] = scrapy_selector.css(
            "#react-tabs-1 > div > li::text"
        ).getall()
        amazon["product_catlog"] = scrapy_selector.css(
            "div.breadcrumb > a::text"
        ).getall()
        amazon["product_keywords_2"] = scrapy_selector.css(
            "head > meta[name='description']::attr(content)"
        ).getall()
        browser.quit()

        return amazon


# git push change usage comments
# push 1
