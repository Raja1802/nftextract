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

    name = "etsy"
    rotate_user_agent = True
    allowed_domains = ["www.etsy.com"]
    start_urls = ["https://www.etsy.com/"]

    rules = (Rule(sle(allow="listing/",), callback="parse_images", follow=True,),)

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
        amazon["product_mrp"] = response.css("p.wt-text-strikethrough::text").getall()
        amazon["product_name"] = (
            response.css("div.listing-page-title-component > h1::text").getall()
            or response.css("head > meta[property='og:title']::attr(content)").get()
        )
        amazon["product_description"] = response.css(
            "div#wt-content-toggle-product-details-read-more > p::text"
        ).getall()
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "etsy.com"
        amazon["product_by_name"] = "etsy"
        amazon["product_rating"] = (
            response.css(
                "#listing-page-cart > div > div.wt-mb-xs-1 > div > div > a > span::text"
            ).getall()
            + response.css(
                "#listing-page-cart > div > div.wt-mb-xs-1 > div > div > a > span > span::text"
            ).getall()
        )
        # images = []
        # for image in response.css("div.c-pwa-image-viewer-thumbnails__slider"):
        #     images = images.append(
        #         image.css("a.c-pwa-image-viewer-thumbnails__link::attr(href)").get()
        #     )

        amazon["product_image"] = (
            response.css("head > meta[property='og:image']::attr(content)").get()
            or response.css(
                "head > meta[property='twitter:image']::attr(content)"
            ).get()
        )

        amazon["product_price"] = response.css(
            "#listing-page-cart > div > div > div.wt-display-flex-xs.wt-align-items-center.wt-justify-content-space-between > div > div.wt-display-flex-xs.wt-align-items-center > p.wt-text-title-03.wt-mr-xs-2::text"
        ).getall()
        amazon["product_price_2"] = response.css(
            "head > meta[property='etsymarketplace:price']::attr(content)"
        ).get()
        amazon["product_about"] = response.css(
            "div#description-text-content-toggle::text"
        ).getall()
        amazon["product_keywords"] = response.css(
            "#wt-content-toggle-tags-read-more > ul > li > a::text"
        ).getall()
        amazon["product_catlog"] = (
            response.css(
                "#wt-content-toggle-tags-read-more > ul > li > a::text"
            ).getall()
            # + response.css("ol.o-pwa-breadcrumbs__list > li > a::text").getall()
        )
        amazon["product_keywords_2"] = response.css(
            "head > meta[property='og:description']::attr(content)"
        ).getall()

        return amazon
