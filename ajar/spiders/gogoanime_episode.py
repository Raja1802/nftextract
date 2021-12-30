import scrapy
from ajar.items import gogoanimeEpisode
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
from fake_useragent import UserAgent
CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
ua = UserAgent()
ua.update()
# chrome requirments
# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
# CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "ggepisode"
    rotate_user_agent = True
    allowed_domains = ["gogoanime.so"]
    start_urls = ["https://gogoanime.so/"]
    rules = (Rule(sle(allow="",deny=("/genre/","/sub-category/","/category/")), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse_result(self, response):
        episode = []
        episode = gogoanimeEpisode()
        userAgent = ua.random
        print(userAgent)
        chrome_options.add_argument(f'user-agent={userAgent}')
        PROXY = "socks5://localhost:9150"
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        browser = webdriver.Chrome(
                executable_path=CHROMEDRIVER_PATH,
                chrome_options=chrome_options,
            )
        browser.get(response.url)
        # print(response.url)
        # browser = webdriver.Chrome(
        #     executable_path=os.environ.get("CHROMEDRIVER_PATH"),
        #     chrome_options=chrome_options,
        # )
        # browser.get(response.url)
        # sleep(0.2)
        scrapy_selector = Selector(text=browser.page_source)
        # scrapy_selector = response
        # css selection of html data tags
        # sleep(1)
        ep_url = response.url
        anime_id = scrapy_selector.css("input#movie_id::attr(value)").get()
        anime_name = scrapy_selector.css("div.anime_video_body > h1::text").get()
        server_1 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(1) > a::attr(data-video)").get()
        server_2 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(2) > a::attr(data-video)").get()
        server_3 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(3) > a::attr(data-video)").get()
        server_4 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(4) > a::attr(data-video)").get()
        server_5 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(5) > a::attr(data-video)").get()
        server_6 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(6) > a::attr(data-video)").get()
        server_7 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(7) > a::attr(data-video)").get()
        server_8 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(8) > a::attr(data-video)").get()
        server_9 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(9) > a::attr(data-video)").get()
        server_10 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(10) > a::attr(data-video)").get()
        server_11 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(11) > a::attr(data-video)").get()
        server_12 = scrapy_selector.css("div.anime_video_body > div.anime_muti_link > ul > li:nth-child(12) > a::attr(data-video)").get()
       
        # master push

        # append data to items
        episode["ep_url"] = ep_url
        episode["anime_id"] = anime_id
        episode["name"] = anime_name
        episode["server_1"] = server_1
        episode["server_2"] = server_2
        episode["server_3"] = server_3
        episode["server_4"] = server_4
        episode["server_5"] = server_5
        episode["server_6"] = server_6
        episode["server_7"] = server_7
        episode["server_8"] = server_8
        episode["server_9"] = server_9
        episode["server_10"] = server_10
        episode["server_11"] = server_11
        episode["server_12"] = server_12
        
        # browser.quit()
        return episode


# git push change usage comments
# push 1
