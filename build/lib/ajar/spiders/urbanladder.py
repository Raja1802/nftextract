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

    name = "urbanladder"
    rotate_user_agent = True
    allowed_domains = ["www.urbanladder.com"]
    start_urls = [
        "https://www.urbanladder.com/products/arabia-6-seater-dining-table?sku=FNTBDI11TK10001&src=subcat"
    ]

    rules = (Rule(sle(allow="products",), callback="parse_images", follow=True,),)

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
        sleep(1)
        scrapy_selector = Selector(text=browser.page_source)

        amazon["product_id"] = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_mrp"] = scrapy_selector.css("div.strikeprice > div::text").get()
        amazon["product_name"] = scrapy_selector.css(
            "head > meta[property='og:title']::attr(content)"
        ).get()
        amazon["product_description"] = scrapy_selector.css(
            "#product-description > div > ul > li::text"
        ).getall()
        amazon["product_ASIN"] = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "urbanladder.com"
        amazon["product_by_name"] = "urbanladder"
        amazon["product_rating"] = "NULL"
        images = []
        for image in scrapy_selector.css(
            "#product-left-part-wrap > div.orbit-container.current > ul"
        ):
            images = images.append(image.css("li > img::attr(data-zoom-image)").get())
        amazon["product_image"] = (
            images
            or response.css("head > meta[property='og:image']::attr(content)").get()
        )
        amazon["product_image_2"] = (
              response.css("#product-thumbnails > li:nth-child(2) > a > img::attr(src)").get()
        )
        amazon["product_image_3"] = (
            response.css("#product-thumbnails > li:nth-child(3) > a > img::attr(src)").get()
        )
        amazon["product_image_4"] = (
            response.css("#product-thumbnails > li:nth-child(4) > a > img::attr(src)").get()
        )

        amazon["product_price"] = scrapy_selector.css("div.price::text").get()
        amazon["product_price_2"] = scrapy_selector.css("div.price::text").get()
        amazon["product_about"] = scrapy_selector.css(
            "#product-properties > li > span.property_val > span::text"
        ).getall()
        amazon["product_keywords"] = scrapy_selector.css(
            "div.tab-content  > div.tab-pane:nth-child(3) > ul > li::text"
        ).getall()
        amazon["product_catlog"] = scrapy_selector.css(
            "#breadcrumbs > ul > li > a > span::text"
        ).getall()
        amazon["product_keywords_2"] = scrapy_selector.css(
            "head > meta[name='keywords']::attr(content)"
        ).getall()
        browser.quit()

        return amazon
