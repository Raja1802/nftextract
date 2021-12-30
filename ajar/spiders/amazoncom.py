#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(CrawlSpider):

    name = "amazoncom"
    rotate_user_agent = True
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/"]

    rules = (
        Rule(
            sle(
                allow="/dp/",
                deny=(
                    "/ap/",
                    "/s/",
                    "/gp/",
                    "/hz/",
                    "/b/",
                    "/mn/",
                    "/slp/",
                    "/amazonprime",
                ),
            ),
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
            "span.priceBlockStrikePriceString::text"
        ).get()
        amazon["product_name"] = response.css("#productTitle::text").extract()
        amazon["product_description"] = response.css(
            "#productDescription > p::text"
        ).get()
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "amazon.com"
        amazon["product_by_name"] = "amazon"
        amazon["product_rating"] = response.css("#acrPopover::attr(title)").get()
        amazon["product_image"] = response.css(
            "#imgTagWrapperId > img::attr(data-old-hires)"
        ).get()
        amazon["product_price"] = response.css(
            "span.priceBlockBuyingPriceString::text"
        ).get()
        amazon["product_price_2"] = response.css(
            "#regularprice_savings > td.priceBlockSavingsString::text"
        ).get()
        amazon["product_about"] = response.css(
            "#feature-bullets > ul > li > span.a-list-item::text"
        ).getall()
        amazon["product_keywords"] = response.css(
            "#productDetails_techSpec_section_1 > tbody > tr > td::text"
        ).getall()
        amazon["product_catlog"] = response.css(
            "#wayfinding-breadcrumbs_feature_div > ul > li > span > a::text"
        ).getall()
        amazon["product_keywords_2"] = response.css(
            "head > meta[name='keywords']::attr(content)"
        ).getall()

        return amazon
