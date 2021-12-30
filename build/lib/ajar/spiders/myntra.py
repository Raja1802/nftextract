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
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
PROXY = "socks4://103.88.221.194:46450"
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "myntra"
    # rotate_user_agent = True
    allowed_domains = ["www.myntra.com"]
    start_urls = ["https://www.myntra.com/jeans/levis/levis-women-blue-711-skinny-fit-mid-rise-clean-look-stretchable-jeans/11184534/buy"]
    rules = (Rule(sle(allow="",), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse_result(self, response):
        amazon = []
        amazon = AmazonUs()
        userAgent = ua.random
        chrome_options.add_argument(f'user-agent={userAgent}')
        browser = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(10000)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        product_id = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_mrp = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.pdp-description-container > div.pdp-price-info > p.pdp-discount-container > span.pdp-mrp > s::text"
            ).getall()
            or scrapy_selector.css("span.pdp-mrp > s::text").getall()
        )
        product_description = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.pdp-description-container > div.pdp-productDescriptors > div > div > p.pdp-product-description-content::text"
            ).getall()
            or scrapy_selector.css("p.pdp-product-description-content::text").getall()
            or scrapy_selector.css("head > meta[property='og:description']::attr(content)").getall()
        )
        product_name = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.pdp-description-container > div.pdp-price-info > h1.pdp-name::text"
            ).getall()
            or scrapy_selector.css("h1.pdp-name::text").getall()
            or scrapy_selector.css("head > meta[name='twitter:title']::attr(content)").getall()
        )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.myntra.com"
        product_by_name = "myntra"
        product_rating = "NAN"
        product_image = (
            scrapy_selector.css(
                "head > meta[property='og:image']::attr(content)"
            ).get()
            or scrapy_selector.css("head > meta[name='twitter:image']::attr(content)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.image-grid-container.common-clearfix > div:nth-child(2) > div > div.image-grid-image::attr(style)"
            ).get()
            or scrapy_selector.css("div.image-grid-container > div:nth-child(2) > div > div.image-grid-image::attr(style)").get()
        )
        product_image_3 = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.image-grid-container.common-clearfix > div:nth-child(3) > div > div.image-grid-image::attr(style)"
            ).get()
            or scrapy_selector.css("div.image-grid-container> div:nth-child(3) > div > div.image-grid-image::attr(style)").get()
        )
        product_image_4 = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.image-grid-container.common-clearfix > div:nth-child(4) > div > div.image-grid-image::attr(style)"
            ).get()
            or scrapy_selector.css("div.image-grid-container > div:nth-child(4) > div > div.image-grid-image::attr(style)").get()
        )
        product_price = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.pdp-description-container > div.pdp-price-info > p.pdp-discount-container > span.pdp-price > strong::text"
            ).getall()
            or scrapy_selector.css("span.pdp-price > strong::text").getall()
        )
        product_about = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.pdp-description-container > div.pdp-productDescriptors > div > div:nth-child(2) > p::text"
            ).getall()
            or scrapy_selector.css("p.pdp-sizeFitDescContent::text").getall()
        )
        product_keywords = scrapy_selector.css(
            "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.pdp-description-container > div.pdp-productDescriptors > div > div.index-sizeFitDesc > div > div > div.index-rowValue"
        ).getall()
        product_catlog = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.breadcrumbs-container > a.breadcrumbs-link::text"
            ).getall()
            or scrapy_selector.css("a.breadcrumbs-link::text").getall()
        )
        product_price_2 = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.pdp-description-container > div.pdp-price-info > p.pdp-discount-container > span.pdp-discount::text"
            ).getall()
            or scrapy_selector.css("span.pdp-discount::text").getall()
        )

        product_keywords_2 = (
            scrapy_selector.css(
                "#mountRoot > div > div > div > main > div.pdp-details.common-clearfix > div.pdp-description-container > div.pdp-productDescriptors > div > div:nth-child(3) > p::text"
            ).getall()
            or scrapy_selector.css("div.pdp-productDescriptors > div > div:nth-child(3) > p::text").getall()
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
