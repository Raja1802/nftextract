# -*- coding: utf-8 -*-
import json
import scrapy
from ajar.items import UnsplashApi

class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "unsplash"
    rotate_user_agent = True
    api_url = 'https://unsplash.com/napi/photos?page={}&per_page=100'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data:
            img_id = quote['id']
            alt_description = quote['alt_description']
            categories = quote['categories']
            color = quote['color']
            created_at = quote['created_at']
            current_user_collections = quote['current_user_collections']
            description = quote['description']
            height = quote['height']
            width = quote['width']
            links_download = quote['links']['download']
            links_download_location = quote['links']['download_location']
            links_html = quote['links']['html']
            links_self = quote['links']['self']
            urls_full = quote['urls']['full']
            urls_raw =quote['urls']['raw']
            urls_regular =quote['urls']['regular']
            urls_small = quote['urls']['small']
            urls_thumb = quote['urls']['thumb']
            updated_at = quote['updated_at']
            yield UnsplashApi(img_id=img_id, alt_description=alt_description,categories=categories,color=color,created_at=created_at,updated_at=updated_at,urls_thumb=urls_thumb,urls_small=urls_small,urls_regular=urls_regular,urls_raw=urls_raw,urls_full=urls_full,links_self=links_self,links_html=links_html,links_download_location=links_download_location,links_download=links_download,width=width,height=height,description=description,current_user_collections=current_user_collections,)

        for next_page in range(1, 1000):
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)

            # for x in range(99999):
            #     for next_page in range(x, x + 100):
            #         yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)


            #https://unsplash.com/napi/photos/XWb9XxtMucY