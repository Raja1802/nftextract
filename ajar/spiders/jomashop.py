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
# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
# CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesSpider(CrawlSpider):

    name = "jomashop"
    rotate_user_agent = True
    allowed_domains = ["www.jomashop.com"]
    start_urls = ["https://www.jomashop.com/"]

    rules = (Rule(sle(allow="",), callback="parse_images", follow=True,),)

    def parse_images(self, response):
        amazon = []
        amazon = AmazonUs()
        # browser = webdriver.Chrome(
        #     # executable_path=os.environ.get(CHROMEDRIVER_PATH),
        #     executable_path=os.environ.get("CHROMEDRIVER_PATH"),
        #     chrome_options=chrome_options,
        # )
        # browser.get(response.url)
        # sleep(0.5)
        # scrapy_selector = Selector(text=browser.page_source)

        amazon["product_id"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_mrp"] = response.css(
            "#product_addtocart_form > div.product-essential > div.product-shop > div.col2-set.product-main-col2-set.clearfix > div.col-1 > div.product-type-data-info > div > ul > li.pdp-retail-price > span::text"
        ).getall()
        amazon["product_name"] = (
            response.css(
                "#product_addtocart_form > div.product-essential > div.product-shop > div.product-main-info > h1 > span.product-name::text"
            ).getall()
            or response.css("head > meta[property='og:title']::attr(content)").get()
        )
        amazon["product_description"] = response.css(
            "head > meta[property='og:description']::attr(content)"
        ).getall()
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "jomashop.com"
        amazon["product_by_name"] = "jomashop"
        amazon["product_rating"] = "NULL"
        # images = []
        # for image in response.css("div.c-pwa-image-viewer-thumbnails__slider"):
        #     images = images.append(
        #         image.css("a.c-pwa-image-viewer-thumbnails__link::attr(href)").get()
        #     )

        amazon["product_image"] = (
            response.css("head > meta[property='og:image']::attr(content)").get()
            or response.css("div.MagicSlides > div > a::attr(href)").get()
        )

        amazon["product_price"] = response.css("#final-price::text").getall()
        amazon["product_price_2"] = response.css(
            "#product_addtocart_form > div.product-essential > div.product-shop > div.col2-set.product-main-col2-set.clearfix > div.col-1 > div.product-type-data-info > div > div > div > p.pdp-savings > span::text"
        ).get()
        amazon["product_about"] = response.css(
            "ul.attribute-list > li > div > span::text"
        ).getall()
        amazon["product_keywords"] = response.css(
            "ul.attribute-list > li > div > span::text"
        ).getall()
        amazon["product_catlog"] = (
            response.css(
                "body > div.wrapper > div.page > div.breadcrumbs > ul > li.home > a > span::text"
            ).getall()
            # + response.css("ol.o-pwa-breadcrumbs__list > li > a::text").getall()
        )
        amazon["product_keywords_2"] = response.css(
            "head > meta[property='og:description']::attr(content)"
        ).getall()

        return amazon
