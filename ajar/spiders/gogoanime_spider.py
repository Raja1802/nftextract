import scrapy
from ajar.items import gogoanimeDownload
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import random
# from fake_useragent import UserAgent
CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
# ua = UserAgent()
# ua.update()
# chrome requirments
# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
# CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
# chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "ggspider_dat"
    rotate_user_agent = True
    allowed_domains = ["www3.gogoanime.cm"]
    start_urls = ["https://www3.gogoanime.cm/"]
    rules = (Rule(sle(allow="",deny=("/category/", "/sub-category/", "/genre/")), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse_result(self, response):
        anime = []
        anime = gogoanimeDownload()
        # userAgent = ua.random
        # print(userAgent)
        # chrome_options.add_argument(f'user-agent={userAgent}')
        # PROXY = "socks5://localhost:9150"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--ignore-ssl-errors')
        # browser = webdriver.Chrome(
        #         executable_path=CHROMEDRIVER_PATH,
        #         chrome_options=chrome_options,
        #     )
        # browser.get(response.url)
        # sleep(30)
        # print(response.url)
        # browser = webdriver.Chrome(
        #     executable_path=os.environ.get("CHROMEDRIVER_PATH"),
        #     chrome_options=chrome_options,
        # ) 
        # browser.get(response.url)
        # sleep(0.5)
        # scrapy_selector = Selector(text=browser.page_source)
        scrapy_selector = response
        # css selection of html data tags
        # print(response.url)
        ep_url = response.url
        anime_id = scrapy_selector.css("input#movie_id::attr(value)").get()
        episode_number = scrapy_selector.css("input#default_ep::attr(value)").get()
        alias_anime = scrapy_selector.css("input#alias_anime::attr(value)").get()
        name = scrapy_selector.css("div.anime_video_body > h1::text").get()
        download_1 = scrapy_selector.css("li.dowloads > a::attr(href)").get()
        # master push

        # append data to items
        anime["ep_url"] = ep_url
        anime["anime_id"] = anime_id
        anime["episode_number"] = episode_number
        anime["alias_anime"] = alias_anime
        anime["name"] = name
        anime["download_1"] = download_1

        # browser.quit()
        return anime


# git push change usage comments
# push 1
