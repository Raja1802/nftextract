import scrapy
from ajar.items import gogoanimeDownload
from scrapy.spiders import CrawlSpider, Rule, Simpl
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random

class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "ggspider_dat"
    rotate_user_agent = True
    allowed_domains = ["www3.gogoanime.cm"]
    def parse(self, response):
        anime = []
        anime = gogoanimeDownload()
        scrapy_selector = response
        ep_url = response.url
        anime_id = scrapy_selector.css("input#movie_id::attr(value)").get()
        episode_number = scrapy_selector.css("input#default_ep::attr(value)").get()
        alias_anime = scrapy_selector.css("input#alias_anime::attr(value)").get()
        name = scrapy_selector.css("div.anime_video_body > h1::text").get()
        download_1 = scrapy_selector.css("li.dowloads > a::attr(href)").get()
        anime["ep_url"] = ep_url
        anime["anime_id"] = anime_id
        anime["episode_number"] = episode_number
        anime["alias_anime"] = alias_anime
        anime["name"] = name
        anime["download_1"] = download_1
        return anime

