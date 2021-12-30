# -*- coding: utf-8 -*-
import json
import scrapy
from ajar.items import gogoanimeEpisodeAPI

class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "gogoapil"
    rotate_user_agent = True
    # https://ajax.gogocdn.net/ajax/page-recent-release.html?page=1&type=1
    api_url = 'https://ajax.gogocdn.net/ajax/page-recent-release.html?page={}&type=1'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        # data = json.loads(response.text)
        for li in response.css("ul.items > li"):
            ep_url = li.css('p.name > a::attr(href)').get()
            episode_name = li.css('p.episode::text').get()
            cate = li.css("p.name > a::attr(href)").get()
            vien = li.css("p.name > a::attr(href)").get()
            uri = response.url
            yield gogoanimeEpisodeAPI(ep_url=ep_url, episode_name=episode_name,cate=cate,vien=vien,uri=uri)

        for next_page in range(0, 5):
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)

            # for x in range(99999):
            #     for next_page in range(x, x + 100):
            #         yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)


            #https://unsplash.com/napi/photos/XWb9XxtMucY