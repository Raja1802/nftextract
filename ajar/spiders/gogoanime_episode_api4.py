# -*- coding: utf-8 -*-
import json
import scrapy
from ajar.items import gogoanimeEpisodeAPI

class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "gogoapi_4"
    rotate_user_agent = True
    api_url = 'https://ajax.gogocdn.net/ajax/load-list-episode?ep_start=0&ep_end=10000000000&id={}'
    start_urls = [api_url.format(6000)]

    def parse(self, response):
        # data = json.loads(response.text)
        for li in response.css("ul > li"):
            ep_url = li.css('a::attr(href)').get()
            episode_name = li.css('a > div.name::text').get()
            cate = li.css("a > div.vien::text").get()
            vien = li.css("a > div.cate::text").get()
            uri = response.url
            yield gogoanimeEpisodeAPI(ep_url=ep_url, episode_name=episode_name,cate=cate,vien=vien,uri=uri)

        for next_page in range(6000, 10000):
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)

            # for x in range(99999):
            #     for next_page in range(x, x + 100):
            #         yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)


            #https://unsplash.com/napi/photos/XWb9XxtMucY