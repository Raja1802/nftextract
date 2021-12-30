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
# from fake_useragent import UserAgent
# ua = UserAgent()
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "snpdl"
    rotate_user_agent = True
    allowed_domains = ["www.snapdeal.com"]
    start_urls = ["https://www.snapdeal.com/"]
    rules = (Rule(sle(allow="/product/",), callback="parse_result", follow=True),)
    # sitemap_urls = ["https://www.ajio.com/medias/sys_master/sitemap/sitemap/Product-en-INR-0/Product-en-INR-0.xml"]
    # parsing results with below function
    def parse_result(self, response):
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
                "#buyPriceBox > div.row.reset-margin > div.col-xs-14.reset-padding.padL8 > div.disp-table > div.pdp-e-i-PAY-r.disp-table-cell.lfloat > div.pdpCutPrice::text"
            ).getall()
            or scrapy_selector.css("div.pdpCutPrice::text").getall()
        )
        product_description = (
            scrapy_selector.css(
                "#id-tab-container > div > div:nth-child(3) > div.spec-body > div[itemprop='description']::text"
            ).getall()
            or scrapy_selector.css("div[itemprop='description']::text").getall()
            or scrapy_selector.css("head > meta[property='og:description']::attr(content)").getall()
        )
        product_name = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-4 > div > h1::text"
            ).get()
            or scrapy_selector.css("h1.prod-name::text").get()
            or scrapy_selector.css("head > meta[name='twitter:title']::attr(content)").get()
        )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.snapdeal.com"
        product_by_name = "snapdeal"
        product_rating = "NAN"
        product_image = (
            scrapy_selector.css(
                "head > meta[property='og:image']::attr(content)"
            ).get()
            or scrapy_selector.css("head > meta[name='twitter:image']::attr(content)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "#bx-pager-left-image-panel > a[data-slide-index='0'] > img::attr(src)"
            ).getall()
        )
        product_image_3 = (
            scrapy_selector.css(
                "#bx-pager-left-image-panel > a[data-slide-index='1'] > img::attr(src)"
            ).getall()
        )
        product_image_4 = (
            scrapy_selector.css(
                "#bx-pager-left-image-panel > a[data-slide-index='2'] > img::attr(src)"
            ).get()
        )
        product_price = (
            scrapy_selector.css(
                "#buyPriceBox > div.row.reset-margin > div.col-xs-14.reset-padding.padL8 > div.disp-table > div.pdp-e-i-PAY-r.disp-table-cell.lfloat > span.pdp-final-price > span::text"
            ).getall()
            or scrapy_selector.css("span.pdp-final-price > span::text").getall()
        )
        product_about = (
            scrapy_selector.css(
                "#id-tab-container > div > div.spec-section.expanded.highlightsTileContent > div.spec-body.p-keyfeatures > ul > li> span.h-content::text"
            ).getall()
        )
        product_keywords = scrapy_selector.css(
            "#attribute-select-0 > div.col-xs-21 > div > div > div.pull-left > div > div.attr-val.ellipses-cls::text"
        ).getall()
        product_catlog = (
            scrapy_selector.css(
                "#breadCrumbWrapper > div > a > span::text"
            ).getall()
        )
        product_price_2 = (
            scrapy_selector.css(
                "#buyPriceBox > div.row.reset-margin > div.col-xs-14.reset-padding.padL8 > div.disp-table > div.pdp-e-i-PAY-r.disp-table-cell.lfloat > span.pdpDiscount > span::text"
            ).getall()
            or scrapy_selector.css("span.pdpDiscount > span::text").getall()
        )

        product_keywords_2 = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-4 > div > p.prod-color::text"
            ).getall()
            or scrapy_selector.css("head > meta[name='keywords']::attr(content)").getall()
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
