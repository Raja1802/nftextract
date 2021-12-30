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

    name = "hm"
    rotate_user_agent = True
    allowed_domains = ["www2.hm.com"]
    start_urls = ["https://www2.hm.com/"]

    rules = (Rule(sle(allow="en_us",), callback="parse_images", follow=True,),)

    def parse_images(self, response):
        amazon = []
        amazon = AmazonUs()
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
            "div.product-item-price > span.price-value::text"
        ).getall()
        amazon["product_name"] = (
            scrapy_selector.css("h1.product-item-headline::text").getall()
            or scrapy_selector.css(
                "head > meta[property='og:title']::attr(content)"
            ).get()
        )
        amazon["product_description"] = scrapy_selector.css(
            "p.pdp-description-text::text"
        ).getall()
        amazon["product_ASIN"] = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "https://www2.hm.com/"
        amazon["product_by_name"] = "hm"
        amazon["product_rating"] = "NULL"
        # images = []
        # for image in scrapy_selector.css("div.c-pwa-image-viewer-thumbnails__slider"):
        #     images = images.append(
        #         image.css("a.c-pwa-image-viewer-thumbnails__link::attr(href)").get()
        #     )

        amazon["product_image"] = (
            scrapy_selector.css("head > meta[property='og:image']::attr(content)").get()
            or scrapy_selector.css(
                "head > meta[property='twitter:image']::attr(content)"
            ).get()
        )

        amazon["product_price"] = scrapy_selector.css(
            "div.product-item-price > span.price-value::text"
        ).getall()
        amazon["product_price_2"] = scrapy_selector.css(
            "div.product-item-price > span.price-value::text"
        ).get()
        amazon["product_about"] = scrapy_selector.css(
            "#main-content > div.product.parbase > div.layout.pdp-wrapper.product-detail.sticky-footer-wrapper.js-reviews.fill-me-up > div.module.product-description.sticky-wrapper > div.js-before-secondary-images > div > div > dl > div > dd > ul > li::text"
        ).getall()
        amazon["product_keywords"] = scrapy_selector.css(
            "head > meta[property='og:description']::attr(content)"
        ).getall()
        amazon["product_catlog"] = (
            scrapy_selector.css(
                "#main-content > div.breadcrumb.pdpbreadcrumb > nav > ul > li > a > span::text"
            ).getall()
            # + scrapy_selector.css("ol.o-pwa-breadcrumbs__list > li > a::text").getall()
        )
        amazon["product_keywords_2"] = scrapy_selector.css(
            "div.product-colors > h3::text"
        ).getall()

        return amazon
