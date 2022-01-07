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
    name = "tiffany_products"
    rotate_user_agent = True
    allowed_domains = ["www.tiffany.com"]
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
        sleep(30)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        product_id = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_mrp = (
            scrapy_selector.css(
                "span.product-description__addtobag_btn_text-static_price-wrapper_price::text"
            ).get()
            or scrapy_selector.css("span.price::text").get()
        )
        product_description = (
            scrapy_selector.css(
                "div.product-description__container_detail > p::text"
            ).getall()
               )
        product_name = (
            scrapy_selector.css(
                "h1.product-description__content_title > span::text"
            ).getall()
              )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.tiffany.com"
        product_by_name = "tiffany"
        product_rating = scrapy_selector.css("p.d-sm-ib.pl4-sm::text").getall()
        product_image = (
            scrapy_selector.css(
                "head > meta[property='og:image']::attr(content)"
            ).get()
            or scrapy_selector.css("head > meta[name='twitter:image']::attr(content)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "#main > div > div > div > div.basicproductinformation.parbase.aem-GridColumn.aem-GridColumn--default--12 > div.content-band--60x40.container.pdp-container > div.band-item.base-item.image-init > div > div:nth-child(2) > img::attr(src)"
            ).getall()
        )
        product_image_3 = (
            scrapy_selector.css(
                "#main > div > div > div > div.basicproductinformation.parbase.aem-GridColumn.aem-GridColumn--default--12 > div.content-band--60x40.container.pdp-container > div.band-item.base-item.image-init > div > div:nth-child(3) > img::attr(src)"
            ).getall()
        )
        product_image_4 = (
            scrapy_selector.css(
                "#main > div > div > div > div.basicproductinformation.parbase.aem-GridColumn.aem-GridColumn--default--12 > div.content-band--60x40.container.pdp-container > div.band-item.base-item.image-init > div > div:nth-child(4) > img::attr(src)"
            ).get()
        )
        product_price = (
            scrapy_selector.css("span.product-description__addtobag_btn_text-static_price-wrapper_price::text").get()
        )
        product_about = (
            scrapy_selector.css(
                "#main > div > div > div > div.basicproductinformation.parbase.aem-GridColumn.aem-GridColumn--default--12 > div.content-band--60x40.container.pdp-container > div:nth-child(2) > div > article.product-description.app-js__product-description.right-full-element > div.product-description__container > div.product-description__container_detail > ul.product-description__container_detail_list > li > span.product-description__container_list-content::text"
            ).getall()
        )
        product_keywords = "tiffany, jewelry, branded"
        product_catlog = "tiffany"
        product_price_2 = (
            scrapy_selector.css(
                "span.product-description__addtobag_btn_text-static_price-wrapper_price::text"
            ).getall()
        )

        product_keywords_2 = "tiffany, jewelry, branded"

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
