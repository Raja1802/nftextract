 # -*- coding: utf-8 -*-
import json
import scrapy
from ajar.items import Shopstyles

class QuotesInfiniteScrollSpider(scrapy.Spider):
    i = 1
    name = "shopstyles"
    rotate_user_agent = True
    api_url = 'https://www.shopstyle.com/api/v2/site/productCluster?brandUrlId=yves-salomon-kids&pid=shopstyle&productId={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        
        data = json.loads(response.text)
        yield Shopstyles(url=response.url, response=data)

        if 1==1 and self.i!=910450282:
            self.i = self.i+1
            yield scrapy.Request(url=self.api_url.format(self.i), callback=self.parse)

            # for x in range(99999):
            #     for next_page in range(x, x + 100):
            #         yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)


            #https://unsplash.com/napi/photos/XWb9XxtMucY