import scrapy
from ajar.items import TestItem
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os


# from scrapy_selenium import SeleniumRequest
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = True

# options = Options()
# options.set_headless(headless=True)

# # GEKO = "/app/vendor/geckodriver/geckodriver"
# binary = FirefoxBinary(r"/app/vendor/firefox/firefox")
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
# chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "mint"
    rotate_user_agent = True
    allowed_domains = ["www.nike.com"]
    start_urls = ["https://www.nike.com/"]
    rules = (Rule(sle(allow="/t/",), callback="parse_result", follow=True),)

    # def start_process(self, response):
    #     for url in response.url:
    #         yield SeleniumRequest(
    #             url=url, callback=self.parse_result, wait_time=10,
    #         )
    def parse_result(self, response):
        amazon = []
        amazon = TestItem()
        print(response.url)
        browser = webdriver.Chrome(
            # executable_path=os.environ.get(CHROMEDRIVER_PATH),
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(2)
        scrapy_selector = Selector(text=browser.page_source)
        data = scrapy_selector.css(
            "#RightRail > div > div.css-1ne55sl.mb2-sm > div > div.d-lg-ib.mb0-sm.u-full-width.css-74mc45 > div.headline-5.ta-sm-r.css-1122yjz > div > div::text"
        ).getall()

        amazon["name"] = data
        browser.quit()
        return amazon

        # print(self.start_urls)
        # print(response.selector.xpath("//title/@text"))
        # print(response.request.meta["driver"].title)
        # push test
        # print("hello")
