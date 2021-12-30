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

    name = "walmart"
    rotate_user_agent = True
    allowed_domains = ["www.walmart.com"]
    start_urls = ["https://www.walmart.com/"]

    rules = (Rule(sle(allow=("ip", "p")), callback="parse_images", follow=True,),)

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

        amazon["product_id"] = (
            "https://www.walmart.com"
            + scrapy_selector.css('head > link[rel= "canonical"]::attr(href)').get()
        )
        amazon["product_mrp"] = scrapy_selector.css(
            "span.price--strikethrough > span.visuallyhidden::text"
        ).getall()
        amazon["product_name"] = scrapy_selector.css(
            " h1.prod-ProductTitle::text"
        ).get()
        amazon["product_description"] = scrapy_selector.css(
            "div.about-product-description > ul > li::text"
        ).getall()
        amazon["product_ASIN"] = (
            "https://www.walmart.com"
            + scrapy_selector.css('head > link[rel= "canonical"]::attr(href)').get()
        )
        amazon["product_by_url"] = "walmart.com"
        amazon["product_by_name"] = "walmart"
        amazon["product_rating"] = scrapy_selector.css(
            "span.stars-container::attr(aria-label)"
        ).get()
        # images = []
        # for image in scrapy_selector.css(
        #     "#viewport > div > div > div.Row-uds8za-0.fLedho > div.hezhbt > div > div > div > div.gcDsPc.carouselMainImageWrapper > div > div > div > div.styles__SlideDeckWrapper-beej2j-10.dOAzxY > div"
        # ):
        #     images = images.append(
        #         image.css(
        #             "div > a > div > div > div > div > div > img::attr(src)"
        #         ).get()
        #     )
        amazon["product_image"] = scrapy_selector.css(
            "head > meta[property='og:image']::attr(content)"
        ).get()

        amazon["product_price"] = scrapy_selector.css(
            "div.prod-PriceHero > span > span.price > span.visuallyhidden::text"
        ).getall()
        amazon["product_price_2"] = scrapy_selector.css(
            "span.price > span.visuallyhidden::text"
        ).get()
        amazon["product_about"] = scrapy_selector.css(
            "div.about-product-description::text"
        ).getall()
        amazon["product_keywords"] = scrapy_selector.css(
            "div.about-product-description> li::text"
        ).getall()
        amazon["product_catlog"] = scrapy_selector.css(
            "li.breadcrumb > a > span::text"
        ).getall()
        amazon["product_keywords_2"] = scrapy_selector.css(
            "head > meta[name='keywords']::attr(content)"
        ).getall()
        browser.quit()

        return amazon
