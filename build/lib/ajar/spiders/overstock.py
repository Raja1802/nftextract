#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(CrawlSpider):

    name = "overstock"
    rotate_user_agent = True
    allowed_domains = ["www.overstock.com"]
    start_urls = ["https://www.overstock.com/"]

    rules = (
        Rule(
            sle(allow="", deny=("deals", "store", "dept")),
            callback="parse_images",
            follow=True,
        ),
    )

    def parse_images(self, response):
        amazon = []
        amazon = AmazonUs()

        amazon["product_id"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_mrp"] = response.css(
            "#_1v8PXey > section > div > section > div._3Us5lfj._33u8RpU.price-comparison > span::text"
        ).getall()
        amazon["product_name"] = response.css(
            "#_1v8PXey > section > div > h3._3Bj68d3::text"
        ).extract()
        amazon["product_description"] = response.css(
            "#details > div._2joH_xY > p::text"
        ).get()
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "overstock.com"
        amazon["product_by_name"] = "overstock"
        amazon["product_rating"] = response.css(
            "#_1v8PXey > section > div > section > a::text"
        ).getall()
        amazon["product_image"] = (
            response.css(
                "#image-gallery > div._2Zpskyg > div > div > img::attr(src)"
            ).get()
            or response.css("head > meta[property='og:image']::attr(content)").get()
        )
        amazon["product_price"] = response.css(
            "#product-price-price-container::text"
        ).getall()
        amazon["product_price_2"] = response.css(
            "#_1v8PXey > section > div > section > div._3Us5lfj._1ofMH1A.price-comparison-container > span._1K4khHo::text"
        ).getall()
        amazon["product_about"] = response.css(
            "#details > div._2joH_xY > ul > li::text"
        ).getall()
        amazon["product_keywords"] = response.css(
            "#page > div > section._34cxC8c > section > div > div > div > section > div > div.br62_x7::text"
        ).getall()
        amazon["product_catlog"] = response.css(
            "#breadcrumbSection > span > a::text"
        ).getall()
        amazon["product_keywords_2"] = response.css(
            "head > meta[name='description']::attr(content)"
        ).getall()

        return amazon
