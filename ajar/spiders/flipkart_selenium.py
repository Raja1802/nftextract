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
    name = "flipkart"
    rotate_user_agent = True
    allowed_domains = ["www.flipkart.com"]
    start_urls = []
    #rules = (Rule(sle(allow=( "shirt", "shoes","mobile","cycle","women","men","/p/"), deny=("product-reviews")), callback="parse_result", follow=True),)
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
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._3I9_wc._2p6lqe::text"
            ).getall()
            or scrapy_selector.css("div._3I9_wc._2p6lqe::text").getall()
        )
        product_description = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(6) > div:nth-child(1) > div > div._2418kt > ul > li::text"
            ).get()
            or scrapy_selector.css("div._2418kt > ul > li::text").getall()
        )
        product_name = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div:nth-child(1) > h1 > span::text"
            ).getall()
            or scrapy_selector.css("span.B_NuCI::text").getall()
            or scrapy_selector.css("span.B_NuCI::text").getall()
        )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.flipkart.com"
        product_by_name = "flipkart"
        product_rating = (
            scrapy_selector.css(
                "div._1lRcqv > div::text"
            ).get()
            or scrapy_selector.css("div._3LWZlK::text").get()
        )
        product_image = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-5-12._78xt5Y > div:nth-child(1) > div > div._3li7GG > div._1BweB8 > div._3kidJX > div.CXW8mj._3nMexc > img::attr(src)"
            ).get()
            or scrapy_selector.css("img._396cs4::attr(src)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-5-12._78xt5Y > div:nth-child(1) > div > div._3li7GG > div._35DpL- > div > div._2mLllQ > ul > li:nth-child(2) > div > div::attr(style)"
            ).get()
            or scrapy_selector.css("div._2mLllQ > ul > li:nth-child(2) > div > div::attr(style)").get()
        )
        product_image_3 = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-5-12._78xt5Y > div:nth-child(1) > div > div._3li7GG > div._35DpL- > div > div._2mLllQ > ul > li:nth-child(3) > div > div::attr(style)"
            ).get()
            or scrapy_selector.css("div._2mLllQ > ul > li:nth-child(3) > div > div::attr(style)").get()
        )
        product_image_4 = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-5-12._78xt5Y > div:nth-child(1) > div > div._3li7GG > div._35DpL- > div > div._2mLllQ > ul > li:nth-child(4) > div > div::attr(style)"
            ).get()
            or scrapy_selector.css("div._2mLllQ > ul > li:nth-child(4) > div > div::attr(style)").get()
        )
        product_price = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._30jeq3._16Jk6d::text"
            ).getall()
            or scrapy_selector.css("div._30jeq3._16Jk6d::text").getall()
        )
        product_about = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div:nth-child(3) > div > div._2o-xpa > div._1mXcCf.RmoJUa > p::text"
            ).getall()
            or scrapy_selector.css("div._1mXcCf.RmoJUa > p::text").getall()
        )
        product_keywords = scrapy_selector.css(
            "head > meta[name='Keywords']::attr(content)"
        ).get()
        product_catlog = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div > div > div > div > a._2whKao::text"
            ).getall()
            or scrapy_selector.css("a._2whKao::text").getall()
        )
        product_price_2 = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._3Ay6Sb._31Dcoz > span::text"
            ).getall()
            or scrapy_selector.css("div._3Ay6Sb._31Dcoz > span::text").getall()
        )

        product_keywords_2 = (
            scrapy_selector.css(
                "#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div._1YokD2._3Mn1Gg > div:nth-child(4) > div:nth-child(2) > div > div > div > div > div._3zQntF > p::text"
            ).getall()
            or scrapy_selector.css("div._3zQntF > p::text").getall()
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
