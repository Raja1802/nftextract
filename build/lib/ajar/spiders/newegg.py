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
    name = "newegg"
    rotate_user_agent = True
    allowed_domains = ["www.newegg.com"]
    start_urls = ["https://www.newegg.com/"]
    rules = (Rule(sle(allow="/p/",), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse_result(self, response):
        amazon = []
        amazon = AmazonUs()
        print(response.url)
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
            scrapy_selector.css("#newproductversion > span > strong::text").getall()
            or scrapy_selector.css(
                "#buying-combo > div > div > div > div.buying-combo-info.fix > div.buying-combo-main::attr(data-final-price)"
            ).getall()
        )
        product_description = (
            scrapy_selector.css("#arimemodetail > p::text").getall()
            # or scrapy_selector.css("div._3la3Fn._1zZOAc > p::text").getall()
            # or scrapy_selector.css("div._3la3Fn::text").getall()
        )
        product_name = (
            scrapy_selector.css(
                "head >  meta[property='og:title']::attr(content)"
            ).getall()
            # or scrapy_selector.css("div._3aS5mM > p::text").getall()
            # or scrapy_selector.css("span._35KyD6::text").getall()
        )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.newegg.com"
        product_by_name = "newegg"
        product_rating = "NULL"
        #     scrapy_selector.css(
        #         "#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div > div > div > div > div > span._38sUEc > span > span::text"
        #     ).getall()
        #     or scrapy_selector.css("span._38sUEc > span > span::text").getall()
        # )
        product_image = (
            scrapy_selector.css("head > meta[property='og:image']::attr(content)").get()
            # or scrapy_selector.css("img._1Nyybr.Yun65Y.OGBF1g._30XEf0::attr(src)").get()
        )
        product_price = (
            scrapy_selector.css("#newproductversion > span > strong::text").getall()
            # or scrapy_selector.css("div._1vC4OE._3qQ9m1::text").getall()
        )
        product_about = (
            scrapy_selector.css(
                "head > meta[name='description']::attr(content)"
            ).getall()
            # or scrapy_selector.css("div._3WHvuP > ul > li._2-riNZ::text").getall()
        )
        product_keywords = scrapy_selector.css(
            "head > meta[name='keywords']::attr(content)"
        ).get()
        product_catlog = (
            # scrapy_selector.css(
            #     "#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div > div > div > div > a._1KHd47::text"
            # ).getall()
            scrapy_selector.css("#baBreadcrumbTop > li > a::text").getall()
        )
        product_price_2 = (
            # scrapy_selector.css(
            #     "#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div > div > div._3iZgFn > div._2i1QSc > div > div.VGWI6T._1iCvwn > span::text"
            # ).getall()
            scrapy_selector.css(
                "#landingpage-price > div > div > ul > li.price-current > strong::text"
            ).getall()
        )

        product_keywords_2 = (
            scrapy_selector.css("#Specs > fieldset > dl > dd::text").getall()
            or scrapy_selector.css("div._1aK10F > p::text").getall()
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
