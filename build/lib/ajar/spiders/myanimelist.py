import scrapy
from ajar.items import Myanimelist
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os

from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesSpider(CrawlSpider):

    name = "myanimelist"
    rotate_user_agent = True
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/"]

    rules = (Rule(sle(allow="anime/",), callback="parse_images", follow=True,),)

    def parse_images(self, response):
        anime = []
        anime = Myanimelist()
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(0.5)
        scrapy_selector = Selector(text=browser.page_source)

        anime["anime_name"] = scrapy_selector.css(
            "#contentWrapper > div > h1 > span.h1-title > span::text"
        ).getall()
        anime["anime_discription"] = scrapy_selector.css(
            'span[itemprop="description"]::text'
        ).getall()
        anime["anime_name_english"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(8)::text"
        ).getall()
        anime["anime_name_japanese"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(9)::text"
        ).getall()
        anime["anime_type"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(12) > a::text"
        ).getall()
        anime["anime_episodes"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(13)::text"
        ).getall()
        anime["anime_status"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(14)::text"
        ).getall()
        anime["anime_aired"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(15)::text"
        ).getall()
        anime["anime_primered"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(16) > a::text"
        ).getall()
        anime["anime_broadcast"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(17)::text"
        ).getall()
        anime["anime_producers"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(18) > a::text"
        ).getall()
        anime["anime_licence"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(19) > a::text"
        ).getall()
        anime["anime_studios"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(20) > a::text"
        ).getall()
        anime["anime_source"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(21)::text"
        ).getall()
        anime["anime_gener"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(22) > a::text"
        ).getall()
        anime["anime_durination"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(23)::text"
        ).getall()
        anime["anime_rating"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(24)::text"
        ).getall()
        anime["anime_score"] = scrapy_selector.css(
            '#content > table > tbody > tr > td.borderClass > div > div:nth-child(27) > span[itemprop="ratingValue"]::text'
        ).getall()
        anime["anime_popularity"] = scrapy_selector.css(
            "#content > table > tbody > tr > td.borderClass > div > div:nth-child(29)::text"
        ).getall()
        anime["anime_season"] = scrapy_selector.css(
            "span.information.season > a::text"
        ).getall()
        anime["anime_trailer"] = scrapy_selector.css(
            "div.video-promotion > a::attr(href)"
        ).getall()
        browser.quit()

        return anime
