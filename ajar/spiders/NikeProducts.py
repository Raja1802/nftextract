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
from fake_useragent import UserAgent
ua = UserAgent()
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "nikeus_products"
    rotate_user_agent = True
    allowed_domains = ["www.nike.com"]
    start_urls = []
    # rules = (Rule(sle(allow="/p/", deny=("/c/", )), callback="parse_result", follow=True),)
    #sitemap_urls = ["https://www.pantaloons.com/product-sitemap.xml"]
    # parsing results with below function
    def parse(self, response):
        amazon = []
        amazon = AmazonUs()
        userAgent = ua.random
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        chrome_options.add_argument(f'user-agent={userAgent}')
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(0.2)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        product_id = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_mrp = (
            scrapy_selector.css(
                "div.product-price.is--striked-out::text"
            ).get()
            or scrapy_selector.css("div.product-price.is--current-price::text").get()
        )
        product_description = (
            scrapy_selector.css(
                "div.description-preview > p::text"
            ).getall()
               )
        product_name = (
            scrapy_selector.css(
                "h1#pdp_product_title::text"
            ).getall()
              )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.nike.com"
        product_by_name = "nike"
        product_rating = scrapy_selector.css("p.d-sm-ib.pl4-sm::text").getall()
        product_image = (
            scrapy_selector.css(
                "head > meta[property='og:image']::attr(content)"
            ).get()
            or scrapy_selector.css("head > meta[name='twitter:image']::attr(content)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "#pdp-6-up > button:nth-child(3) > div > picture:nth-child(3) > img::attr(src)"
            ).getall()
        )
        product_image_3 = (
            scrapy_selector.css(
                "#pdp-6-up > button:nth-child(4) > div > picture:nth-child(3) > img::attr(src)"
            ).getall()
        )
        product_image_4 = (
            scrapy_selector.css(
                "#pdp-6-up > button:nth-child(5) > div > picture:nth-child(3) > img::attr(src)"
            ).get()
        )
        product_price = (
            scrapy_selector.css("div.product-price.is--current-price::text").get()
        )
        product_about = (
            scrapy_selector.css(
                "div[data-test='inline-product-description'] > div > div >p::text"
            ).getall()
        )
        product_keywords = "nike, shoes, tshirts"
        product_catlog = "nike"
        product_price_2 = (
            scrapy_selector.css(
                "#RightRail > div > div:nth-child(1) > div > div.d-lg-ib.mb0-sm.u-full-width.css-3rkuu4.css-1mzzuk6 > div > div > span::text"
            ).getall()
        )

        product_keywords_2 = "nike, shoes, tshirts, running"

        # append data to items
        amazon["product_id"] = product_id
        amazon["product_mrp"] = product_mrp
        amazon["product_description"] = product_description
        amazon["product_name"] = product_name
        amazon["product_ASIN"] = product_ASIN
        amazon["product_by_url"] = product_by_url
        amazon["product_by_name"] = product_by_name
        amazon["product_rating"] = product_rating
        amazon["product_image"] = product_image
        amazon["product_image_2"] = product_image_2
        amazon["product_image_3"] = product_image_3
        amazon["product_image_4"] = product_image_4
        amazon["product_price"] = product_price
        amazon["product_about"] = product_about
        amazon["product_keywords"] = product_keywords
        amazon["product_catlog"] = product_catlog
        amazon["product_price_2"] = product_price_2
        amazon["product_keywords_2"] = product_keywords_2
        browser.quit()
        return amazon


####
