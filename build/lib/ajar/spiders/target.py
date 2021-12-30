import scrapy
from ajar.items import AmazonUs
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os


# from scrapy_selenium import SeleniumRequest
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = True

# options = Options()
# options.set_headless(headless=True)

# # GEKO = "/app/vendor/geckodriver/geckodriver"
# binary = FirefoxBinary(r"/app/vendor/firefox/firefox")
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesSpider(CrawlSpider):

    name = "target"
    rotate_user_agent = True
    allowed_domains = ["www.target.com"]
    start_urls = ["https://www.target.com/"]

    rules = (
        Rule(
            sle(allow="p", deny=("/c/", "/s/", "/b/", "/s1/")),
            callback="parse_images",
            follow=True,
        ),
    )

    def parse_images(self, response):
        amazon = []
        amazon = AmazonUs()
        print(response.url)
        browser = webdriver.Chrome(
            # executable_path=os.environ.get(CHROMEDRIVER_PATH),
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(0.5)
        scrapy_selector = Selector(text=browser.page_source)

        amazon["product_id"] = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_mrp"] = scrapy_selector.css(
            "span[data-test='product-savings']::text"
        ).getall()
        amazon["product_name"] = (
            scrapy_selector.css("h1[data-test='product-title']::text").get()
            or scrapy_selector.css(
                "head > meta[property='twitter:title']::attr(content)"
            ).get()
        )
        amazon["product_description"] = scrapy_selector.css(
            "#specAndDescript > div > div.hezhbt > div::text"
        ).getall()
        amazon["product_ASIN"] = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "target.com"
        amazon["product_by_name"] = "target"
        amazon["product_rating"] = scrapy_selector.css(
            "#ratingReviewId > div > span > span::text"
        ).get()

        amazon["product_image"] = (
            scrapy_selector.css("head > meta[property='og:image']::attr(content)").get()
            or scrapy_selector.css(
                "head > meta[property='twitter:image']::attr(content)"
            ).get()
        )

        amazon["product_price"] = scrapy_selector.css(
            "div[data-test='product-price']::text"
        ).getall()
        amazon["product_price_2"] = scrapy_selector.css(
            "div[data-test='product-price']::text"
        ).get()
        amazon["product_about"] = scrapy_selector.css(
            "#tabContent-tab-Details > div > div > div > div.fLedho > div > div > ul > div > div > li > span::text"
        ).getall()
        amazon["product_keywords"] = scrapy_selector.css(
            "#specAndDescript > div> div.hezhbt> div > div::text"
        ).getall()
        amazon["product_catlog"] = scrapy_selector.css(
            "div[data-test='breadcrumb'] > span > a > span::text"
        ).getall()
        amazon["product_keywords_2"] = scrapy_selector.css(
            "head > meta[property='twitter:description']::attr(content)"
        ).getall()
        browser.quit()

        return amazon
