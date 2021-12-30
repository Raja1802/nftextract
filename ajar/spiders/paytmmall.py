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

# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "pytml"
    rotate_user_agent = True
    allowed_domains = ["paytmmall.com"]
    start_urls = []
    #rules = (Rule(sle(allow="pdp",), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse(self, response):
        amazon = []
        amazon = AmazonUs()
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(0.5)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        product_id = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_mrp = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div._39b7 > div > div._19Zj._9qaO > div._3t7S > div._3bvo > div._2viE > div > div._2LVL > span._2b_6::text"
            ).getall()
            or scrapy_selector.css("span._2b_6::text").getall()
        )
        product_description = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div.r3Vi > div > div:nth-child(2) > div._1jlE._15sE > div > div.wJuG._1CXW > div > div._2LOI::text"
            ).getall()
            or scrapy_selector.css("div._2LOI::text").getall()
        )
        product_name = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div._39b7 > div > div._19Zj._9qaO > div._3t7S > div._3bvo > div._2viE > h1::text"
            ).getall()
            or scrapy_selector.css("div._2viE > h1::text").getall()
            or scrapy_selector.css("div._2viE > h1::text").getall()
        )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.paytmmall.com"
        product_by_name = "paytmmall"
        product_rating = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div._39b7 > div > div._19Zj._9qaO > div._3t7S > div._3bvo > div._2viE > div > div:nth-child(3) > div > div._2dWu::text"
            ).getall()
            or scrapy_selector.css("div._2dWu::text").getall()
        )
        product_image = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div._39b7 > div > div.pwO4 > div > div._1a-K > img::attr(src)"
            ).get()
            or scrapy_selector.css("img._3v_O::attr(src)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div._39b7 > div > div.pwO4 > div > div._1uqt > div > div._2soi > div > div._3_E6 > img::attr(src)"
            ).get()
            or scrapy_selector.css("div._2soi > div > div:nth-child(2) > img::attr(src)").get()
        )
        product_image_3 = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div._39b7 > div > div.pwO4 > div > div._1uqt > div > div._2soi > div > div:nth-child(3) > img::attr(src)"
            ).get()
            or scrapy_selector.css("div._2soi > div > div:nth-child(3) > img::attr(src)").get()
        )
        product_image_4 = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div._39b7 > div > div.pwO4 > div > div._1uqt > div > div._2soi > div > div:nth-child(4) > img::attr(src)"
            ).get()
            or scrapy_selector.css("div._2soi > div > div:nth-child(4) > img::attr(src)").get()
        )
        product_price = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div._39b7 > div > div._19Zj._9qaO > div._3t7S > div._3bvo > div._2viE > div > div._2LVL > span._1V3w::text"
            ).getall()
            or scrapy_selector.css("span._1V3w::text").getall()
        )
        product_about = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div.r3Vi > div > div:nth-child(3) > div._1jlE._15sE > div._1MQ4::text"
            ).getall()
            or scrapy_selector.css("div._1jlE._15sE > div._1MQ4::text").getall()
        )
        product_keywords = scrapy_selector.css(
            "head > meta[name='Keywords']::attr(content)"
        ).get()
        product_catlog = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1z-E > div > span > a > span::text"
            ).getall()
            or scrapy_selector.css("a.Tk9i > span::text").getall()
        )
        product_price_2 = (
            scrapy_selector.css(
                "#app > div > div._2Bze > div > div._1D6j > div > div._2rYD > div._39b7 > div > div._19Zj._9qaO > div._3t7S > div._3bvo > div._2viE > div > div._2LVL > span._3llF::text"
            ).getall()
            or scrapy_selector.css("span._3llF::text").getall()
        )

        product_keywords_2 = (
            scrapy_selector.css(
                "a._1Kbo::text"
            ).getall()
            or scrapy_selector.css("a._1Kbo::text").getall()
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