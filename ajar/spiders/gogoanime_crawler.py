import scrapy
from ajar.items import gogoanimeAnime
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# import random
# from fake_useragent import UserAgent
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
# chrome_options = webdriver.ChromeOptions()
# ua = UserAgent()
# ua.update()
# chrome requirments
# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
# CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "ggcr"
    rotate_user_agent = True
    allowed_domains = ["ajax.gogocdn.net"]
    start_urls = ["https://ajax.gogocdn.net/"]
    rules = (Rule(sle(allow="",), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse_result(self, response):
        anime = []
        anime = gogoanimeAnime()
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
        print(response.url)
        anime_id = scrapy_selector.css("input#movie_id::attr(value)").get()
        anime_name = scrapy_selector.css("div.anime_info_body_bg > h1::text").getall() or scrapy_selector.css("div.anime_info_episodes > h2::text").getall()
        anime_image = scrapy_selector.css("div.anime_info_body_bg > img::attr(src)").get()
        anime_season_type = scrapy_selector.css("div.anime_info_body_bg > p:nth-child(4) > a::text").get()
        anime_plot_summary = scrapy_selector.css("div.anime_info_body_bg > p:nth-child(5)::text").get()
        anime_genre = scrapy_selector.css("div.anime_info_body_bg > p:nth-child(6) > a::text").getall()
        anime_released = scrapy_selector.css("div.anime_info_body_bg > p:nth-child(7)::text").get()
        anime_status = scrapy_selector.css("div.anime_info_body_bg > p:nth-child(8) > a::text").get()
        anime_total_episodes = scrapy_selector.css("#episode_page > li > a::attr(ep_end)").get()
        anime_other_names = scrapy_selector.css("div.anime_info_body_bg > p:nth-child(9)::text").getall()
       
        # master push

        # append data to items
        anime["anime_id"] = anime_id
        anime["name"] = anime_name
        anime["image"] = anime_image
        anime["season_type"] = anime_season_type
        anime["plot_summary"] = anime_plot_summary
        anime["genre"] = anime_genre
        anime["released"] = anime_released
        anime["status"] = anime_status
        anime["total_episodes"] = anime_total_episodes
        anime["other_names"] = anime_other_names
        
        
        # browser.quit()
        return anime


# git push change usage comments
# push 1
