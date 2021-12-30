import scrapy
from ajar.items import LinkExtracters
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
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
PROXY = "socks5://localhost:9150"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(scrapy.Spider):
    i = 1
    name = "flipkart_Link"
    rotate_user_agent = True
    url_point = "https://www.flipkart.com/air-conditioners/pr?sid=c54&otracker=categorytree&page="
    api_url = url_point + "{}"
    start_urls = [api_url.format(1)]
    # allowed_domains = ["www.flipkart.com"]
    # start_urls = ["https://www.flipkart.com/"]
    # rules = (Rule(sle(allow=( "shirt", "shoes","mobile","cycle","women","men","/p/"), deny=("product-reviews")), callback="parse_result", follow=True),)
    # parsing results with below function
    def seleniumparse(self, url):
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(url)
        # sleep(0.5)
        # 
        return Selector(text=browser.page_source)
        browser.quit()
    def parse(self, response):        
        scrapy_selector = self.seleniumparse(response.url)
        # scrapy_selector = response
        for j in scrapy_selector.css("div._1AtVbE"):
            url = j.css("a.s1Q9rs::attr(href)").get() or "NAN"
            yield LinkExtracters(url=url, website="flipkart.com")
        if 1==1 and self.i!=48:
            self.i = self.i+1
            yield scrapy.Request(url=self.api_url.format(self.i), callback=self.parse)
        # css selection of html data tags
        # browser.quit()

# git push change usage comments
# push 1
