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
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
PROXY = "socks5://localhost:9050"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "ajio"
    rotate_user_agent = True 
    allowed_domains = ["www.ajio.com"]
    start_urls = ["https://www.ajio.com/"]
    rules = (Rule(sle(allow="",), callback="parse_result", follow=True),)
    # for url in start_urls:
    #     scrapy.Request(url=url, callback=parse_result)
    # sitemap_urls = ["https://www.ajio.com/medias/sys_master/sitemap/sitemap/Product-en-INR-0/Product-en-INR-0.xml"]
    # parsing results with below function
    def parse_result(self, response):
        amazon = []
        amazon = AmazonUs()
        userAgent = ua.random
        chrome_options.add_argument(f'user-agent={userAgent}')
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(1)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        product_id = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_mrp = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-4 > div > div.prod-price-section > div.prod-price-sec > span.prod-cp::text"
            ).getall()
            or scrapy_selector.css("span.prod-cp::text").getall()
        )
        product_description = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-4 > div > section > h2 > ul > li::text"
            ).getall()
            or scrapy_selector.css("li.detail-list::text").getall()
            or scrapy_selector.css("head > meta[property='og:description']::attr(content)").getall()
        )
        product_name = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-4 > div > h1::text"
            ).getall()
            or scrapy_selector.css("h1.prod-name::text").getall()
            or scrapy_selector.css("head > meta[name='twitter:title']::attr(content)").getall()
        )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.ajio.com"
        product_by_name = "ajio"
        product_rating = "NAN"
        product_image = (
            scrapy_selector.css(
                "head > meta[property='og:image']::attr(content)"
            ).get()
            or scrapy_selector.css("head > meta[name='twitter:image']::attr(content)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-6 > div > div.img-mv-left.col-10 > div.image-slick-container > div > div > div > div.slick-slide > div > img::attr(src)"
            ).get()
            or scrapy_selector.css("div.slick-slide > div > img::attr(src)").get()
        )
        product_image_3 = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-6 > div > div.img-mv-left.col-10 > div.image-slick-container > div > div > div > div:nth-child(2) > div > img::attr(src)"
            ).get()
            or scrapy_selector.css("div.image-slick-container > div > div > div > div:nth-child(2) > div > img::attr(src)").get()
        )
        product_image_4 = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-6 > div > div.img-mv-left.col-10 > div.image-slick-container > div > div > div > div:nth-child(3) > div > img::attr(src)"
            ).get()
            or scrapy_selector.css("div.image-slick-container > div > div > div > div:nth-child(3) > div > img::attr(src)").get()
        )
        product_price = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-4 > div > div.prod-price-section > div.prod-sp::text"
            ).getall()
            or scrapy_selector.css("div.prod-sp::text").getall()
        )
        product_about = (
            scrapy_selector.css(
                "#brandDetails > div > div.brand-desc > div::text"
            ).getall()
            or scrapy_selector.css("div.brand-desc > div::text").getall()
        )
        product_keywords = scrapy_selector.css(
            "#appContainer > div.content > div > div > div.breadcrumb-section > ul > li > a::text"
        ).getall()
        product_catlog = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.breadcrumb-section > ul > li > a::text"
            ).getall()
            or scrapy_selector.css("div.breadcrumb-section > ul > li > a::text").getall()
        )
        product_price_2 = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-4 > div > div.prod-price-section > div.prod-price-sec > span.prod-discnt::text"
            ).getall()
            or scrapy_selector.css("span.prod-discnt::text").getall()
        )

        product_keywords_2 = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-4 > div > p.prod-color::text"
            ).getall()
            or scrapy_selector.css("p.prod-color::text").getall()
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
