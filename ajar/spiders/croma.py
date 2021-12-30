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
from fake_useragent import UserAgent
ua = UserAgent()
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
PROXY = "socks5://localhost:9050"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "croma"
    rotate_user_agent = True
    allowed_domains = ["www.croma.com"]
    start_urls = ["https://www.croma.com/"]
    rules = (Rule(sle(allow=(""), deny=("/c/")), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse_result(self, response):
        amazon = []
        amazon = AmazonUs()
        # userAgent = ua.random
        # chrome_options.add_argument(f'user-agent={userAgent}')
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        product_id = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_mrp = (
            scrapy_selector.css(
                "#old-price::text"
            ).get()
            or scrapy_selector.css("#old-price::text").get()
        )
        product_description = (
            scrapy_selector.css(
                "div.MuiCollapse-wrapperInner > #panel5bh-content > div > span > div > ul > li::text"
            ).getall()
            or scrapy_selector.css("div.MuiCollapse-wrapperInner > #panel5bh-content > div > span > div > ul > li::text").getall()
        )
        product_name = (
            scrapy_selector.css(
                "h1.pd-title::text"
            ).getall()
            or scrapy_selector.css("h1.pd-title::text").getall()
            or scrapy_selector.css("h1.pd-title::text").getall()
        )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.croma.com"
        product_by_name = "croma"
        product_rating = (
            scrapy_selector.css(
                "span.MuiRating-readOnly::attr(aria-label)"
            ).get()
            or scrapy_selector.css("span.MuiRating-readOnly::attr(aria-label)").get()
        )
        product_image = (
            scrapy_selector.css(
                "#0prod_img::attr(src)"
            ).get()
            # or scrapy_selector.css("img._396cs4::attr(src)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "#1prod_img::attr(src)"
            ).get()
            # or scrapy_selector.css("div._2mLllQ > ul > li:nth-child(2) > div > div::attr(style)").get()
        )
        product_image_3 = (
            scrapy_selector.css(
                "#2prod_img::attr(src)"
            ).get()
            # or scrapy_selector.css("div._2mLllQ > ul > li:nth-child(3) > div > div::attr(style)").get()
        )
        product_image_4 = (
            scrapy_selector.css(
                "#3prod_img::attr(src)"
            ).get()
            # or scrapy_selector.css("div._2mLllQ > ul > li:nth-child(4) > div > div::attr(style)").get()
        )
        product_price = (
            scrapy_selector.css(
                "#pdpdatael > div:nth-child(2) > div.container > div > div > div > div.col-md-6.right-alignElement > div > ul > li:nth-child(1) > div.cp-price.main-product-price > span.new-price > span.amount::text"
            ).getall()
            or scrapy_selector.css(" span.new-price > span.amount::text").get()
        )
        product_about = (
            scrapy_selector.css(
                "div.MuiCollapse-wrapperInner > #panel1bh-content > div > span > div > ul > li > strong::text"
            ).getall()
            # or scrapy_selector.css("div._1mXcCf.RmoJUa > p::text").getall()
        )
        product_keywords = scrapy_selector.css(
            "head > meta[name='Keywords']::attr(content)"
        ).get()
        product_catlog = (
            scrapy_selector.css(
                "#pdpdatael > div.cp-breadcrumb > div > ul > li > a::text"
            ).getall()
            # or scrapy_selector.css("a._2whKao::text").getall()
        )
        product_price_2 = "NAN"

        product_keywords_2 = (
            scrapy_selector.css(
                "div.MuiCollapse-wrapperInner > #panel1bh-content > div > span > div > p::text"
            ).getall()
            or scrapy_selector.css("div.MuiCollapse-wrapperInner > #panel1bh-content > div > span > div > p::text").getall()
        )

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


# git push change usage comments
# push 2
