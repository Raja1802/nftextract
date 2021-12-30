#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(CrawlSpider):

    name = "koovs"
    rotate_user_agent = True
    allowed_domains = ["www.koovs.com"]
    start_urls = ["https://www.koovs.com/"]

    rules = (
        Rule(
            sle(allow="", deny=("/tags/", "/brand/", "/women/")),
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
        amazon["product_mrp"] = (
            response.css("span.pd-price::text").get()
            or response.css("span.pd-price-striked::text").get()
        )
        amazon["product_name"] = response.css("div.product-name::text").get()
        amazon["product_description"] = response.css(
            "head > meta[name='description']::attr(content)"
        ).get()
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "https://www.koovs.com/"
        amazon["product_by_name"] = response.css("div.product-brand-name::text").get()
        amazon["product_rating"] = "NULL"
        amazon["product_image"] = response.css(
            'head > meta[name="twitter:image"]::attr(content)'
        ).get()
        amazon["product_price"] = response.css(
            "div.pd-discount-content > div.pd-discount-price::text"
        ).get()
        amazon["product_price_2"] = response.css(
            "div.pd-discount-content > div.pd-discount-percent::text"
        ).get()
        amazon["product_about"] = response.css(
            "div.info-care > div > div > ul > li::text"
        ).getall()
        amazon["product_keywords"] = response.css(
            "head > meta[name='keywords']::attr(content)"
        ).getall()
        amazon["product_catlog"] = response.css(
            "div.breadcrumb > ul > li > div > span > a::text"
        ).getall()
        amazon["product_keywords_2"] = response.css("#slide-1 > div::text").getall()

        return amazon
