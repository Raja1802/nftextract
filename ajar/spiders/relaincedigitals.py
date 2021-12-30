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
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "rlcdig"
    rotate_user_agent = True
    allowed_domains = ["www.reliancedigital.in"]
    start_urls = []
    #rules = (Rule(sle(allow="/p/",deny=("/c/", )), callback="parse_result", follow=True),)
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
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        product_id = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_mrp = (
            scrapy_selector.css(
                "#root > main > main > div.pb__20 > section.pdpStickyContainer > div.blk__sm__7.pdp__topBlock > div > div > div.pdp__priceSection > ul > li > span.pdp__mrpPrice::text"
            ).getall()
            or scrapy_selector.css("span.pdp__offerPrice::text").get()
        )
        product_description = (
            scrapy_selector.css(
                "#root > main > main > div.pb__20 > section.pdpStickyContainer > div.blk__sm__7.pdp__topBlock > div:nth-child(5) > div.blk__sm__6.pdp__featuresBlk > div:nth-child(1) > div.sc-kEYyzF.hQlMfi > div > ul > li > span::text"
            ).getall()
            or scrapy_selector.css("div.sc-kEYyzF.hQlMfi > div > ul > li > span::text").getall()
        )
        product_name = (
            scrapy_selector.css(
                "#root > main > main > div.pb__20 > section.pdpStickyContainer > div.blk__sm__7.pdp__topBlock > div.pdp__title::text"
            ).getall()
            or scrapy_selector.css("div.pdp__title::text").getall()
            or scrapy_selector.css("div.pdp__title::text").getall()
        )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.reliancedigital.in"
        product_by_name = "reliancedigital"
        product_rating = "NAN"
        product_image = (
            scrapy_selector.css(
                "#myimage::attr(data-srcset)"
            ).get()
            or scrapy_selector.css("#myimage::attr(data-srcset)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "div[data-index='1'] > div >#RIl_undefined > div > div > img::attr(data-srcset)"
            ).get()
            or scrapy_selector.css("div[data-index='1'] > div >#RIl_undefined > div > div > img::attr(data-srcset)").get()
        )
        product_image_3 = (
            scrapy_selector.css(
                "div[data-index='2'] > div >#RIl_undefined > div > div > img::attr(data-srcset)"
            ).get()
            or scrapy_selector.css("div[data-index='2'] > div >#RIl_undefined > div > div > img::attr(data-srcset)").get()
        )
        product_image_4 = (
            scrapy_selector.css(
                "div[data-index='3'] > div >#RIl_undefined > div > div > img::attr(data-srcset)"
            ).get()
            or scrapy_selector.css("div[data-index='3'] > div >#RIl_undefined > div > div > img::attr(data-srcset)").get()
        )
        product_price = (
            scrapy_selector.css(
                "span.pdp__offerPrice::text"
            ).get()
            or scrapy_selector.css("span.pdp__offerPrice::text").get()
        )
        product_about = (
            scrapy_selector.css(
                "div.pdp__tab-info::text"
            ).getall()
            or scrapy_selector.css("div.pdp__tab-info::text").getall()
        )
        product_keywords = scrapy_selector.css(
            "head > meta[name='Keywords']::attr(content)"
        ).get()
        product_catlog = (
            scrapy_selector.css(
                "div.bc__breadcrumbMain > span::text"
            ).getall()
            or scrapy_selector.css("div.bc__breadcrumbMain > span::text").getall()
        )
        product_price_2 = (
            scrapy_selector.css(
                "#root > main > main > div.pb__20 > section.pdpStickyContainer > div.blk__sm__7.pdp__topBlock > div:nth-child(5) > div:nth-child(2) > div.pdp__priceSection > ul > li.pdp__priceSection__priceListText.pdp__savePrice::text"
            ).getall()
            or scrapy_selector.css("li.pdp__savePrice::text").getall()
        )

        product_keywords_2 = (
            scrapy_selector.css(
                "div.pdp__tab-info__list__value::text"
            ).getall()
            or scrapy_selector.css("div.pdp__tab-info__list__value::text").getall()
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
# push 1

# 