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

    name = "homedepot"
    # rotate_user_agent = True
    allowed_domains = ["www.homedepot.com"]
    start_urls = [
        "https://www.homedepot.com/p/Noble-House-Somerville-Chesterfield-Navy-Blue-and-Dark-Brown-Sofa-65582/312447366"
    ]

    rules = (
        Rule(
            sle(allow="p", deny=("/c/", "/b2b/", "/b/", "/services/", "/l/")),
            callback="parse_images",
            follow=True,
        ),
    )

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
            "#was-price > div.price-detailed__was-price > span > span::text"
        ).getall()
        amazon["product_name"] = (
            response.css(
                "#root > div > div > div > div.grid.productmarquee.flush > div > div > div > div > div.product-title > h1::text"
            ).getall()
            or response.css("head > meta[property='og:title']::attr(content)").get()
        )
        amazon["product_description"] = (
            response.css(
                "#root > div > div > div > div.grid.productmarquee.flush > div.col__12-12.col__5-12--sm > div:nth-child(2) > div > div > div.preview__lines::text"
            ).getall()
            or response.css(" div.preview__lines::text").getall()
        )
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "homedepot.com"
        amazon["product_by_name"] = "homedepot"
        amazon["product_rating"] = response.css(
            "#root > div > div > div > div.grid.productmarquee.flush > div > div > div > div > div.product-details__review > div.product-details__rating-favcount > div > span::text"
        ).getall()
        # images = []
        # for image in response.css("div.c-pwa-image-viewer-thumbnails__slider"):
        #     images = images.append(
        #         image.css("a.c-pwa-image-viewer-thumbnails__link::attr(href)").get()
        #     )

        amazon["product_image"] = response.css(
            "#media-gallery > div > div > div.mediagallery__mainimage > div > a > div > img::attr(src)"
        ).get()

        amazon["product_price"] = (
            response.css("#was-price > div.price > div > span:nth-child(2)::text").get()
            or response.css(
                "#standard-price > div > div > span:nth-child(2)::text"
            ).get()
        )
        # root > div > div > div > div:nth-child(6) > div > div > div.fbt__prodcontainer > div:nth-child(1) > div > div > div > label > div.fbtProductLine__priceContainer > span > span.fbtProductLine__price
        amazon["product_price_2"] = response.css(
            "#root > div > div > div > div:nth-child(6) > div > div > div.fbt__prodcontainer > div:nth-child(1) > div > div > div > label > div.fbtProductLine__priceContainer > span > span.fbtProductLine__price::text"
        ).get()
        amazon["product_about"] = response.css(
            "#product_description > div.desktop-items > div.grid > div > div > ul > li > span::text"
        ).getall()
        amazon["product_keywords"] = response.css(
            "#specifications > div > div > div > div > div > div::text"
        ).getall()
        amazon["product_catlog"] = (
            response.css("#breadcrumb > ul > li > a::text").getall()
            # + response.css("ol.o-pwa-breadcrumbs__list > li > a::text").getall()
        )
        amazon["product_keywords_2"] = response.css(
            "head > meta[property='og:description']::attr(content)"
        ).getall()

        return amazon
