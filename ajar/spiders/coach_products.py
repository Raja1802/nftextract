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
    name = "coach_products"
    rotate_user_agent = True
    allowed_domains = ["www.coach.com"]
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
        ).get() or response.url
        product_mrp = (
            scrapy_selector.css(
                "div.prices > div > span > span > span.value::text"
            ).get()
            or scrapy_selector.css("div.price > span > span > span.value::text").get()
        )
        product_description = (
            scrapy_selector.css(
                "div.pdp__product-details-desc > li::text"
            ).getall()
               )
        product_name = (
            scrapy_selector.css(
                "p.product-name::text"
            ).get()
              )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.coach.com"
        product_by_name = "coach"
        product_rating = "NA"
        product_image = (
            scrapy_selector.css(
                "head > meta[property='og:image']::attr(content)"
            ).get()
            or scrapy_selector.css("head > meta[name='twitter:image']::attr(content)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "div.pdp-carousel__nav-container.d-none.d-md-block > div.pdp-carousel__nav.js-slider-nav.slick-initialized.slick-slider.slick-vertical > div > div > div:nth-child(5) > div > button > picture > source:nth-child(1)::attr(srcset)"
            ).getall()
        )
        product_image_3 = (
            scrapy_selector.css(
                "div.pdp-carousel__nav-container.d-none.d-md-block > div.pdp-carousel__nav.js-slider-nav.slick-initialized.slick-slider.slick-vertical > div > div > div:nth-child(6) > div > button > picture > source:nth-child(1)::attr(srcset)"
            ).getall()
        )
        product_image_4 = (
            scrapy_selector.css(
                "div.pdp-carousel__nav-container.d-none.d-md-block > div.pdp-carousel__nav.js-slider-nav.slick-initialized.slick-slider.slick-vertical > div > div > div:nth-child(7) > div > button > picture > source:nth-child(1)::attr(srcset)"
            ).get()
        )
        product_price = (
            scrapy_selector.css("div.prices > div > span > span > span.value::text").get()
        )
        product_about = (
            scrapy_selector.css(
                "p.product-desc::text"
            ).getall()
        )
        product_keywords = "coach, fashion, watches, jewellery, branded"
        product_catlog = "www.coach.com"
        product_price_2 = (
            scrapy_selector.css(
                "div.price > span > span > span.value::text"
            ).getall()
        )

        product_keywords_2 = "coach, fashion, watches, jewellery, branded"

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