#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(CrawlSpider):

    name = "pumain"
    rotate_user_agent = True
    allowed_domains = ["in.puma.com"]
    start_urls = ["https://in.puma.com/"]

    rules = (Rule(sle(allow="",), callback="parse_images", follow=True),)

    def parse_images(self, response):
        amazon = []
        amazon = AmazonUs()
        amazon["product_id"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_mrp"] = (response.css(
            "body > div.page > div.product-detail-root > div.product-page-layout > div.product-details-section > div.product-details-col.col-lg-4 > div > div.row.margin-bottom-60 > div.col-md-5 > div > div > div:nth-child(1) > div > span.strike-through.list > span::text"
        ).get() or response.css("span.strike-through > span::text").get())
        amazon["product_name"] = (response.css(
            "body > div.page > div.product-detail-root > div.product-page-layout > div.product-details-section > div.product-details-col.col-lg-4 > div > div.row.margin-bottom-60 > div.col-md-7 > h1::text"
        ).get() or response.css("h1.product-name::text").get())
        amazon["product_description"] = response.css(
            "head > meta[name='description']::attr(content)"
        ).get()
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "https://in.puma.com/"
        amazon["product_by_name"] = "puma.com"
        amazon["product_rating"] = "NULL"
        amazon["product_image"] = response.css(
            'head > meta[property="twitter:image"]::attr(content)'
        ).get()
        amazon["product_image_2"] = response.css(
            'div.image-container > a > picture > source::attr(srcset)'
        ).get()
        amazon["product_image_3"] = response.css(
            'body > div.page > div.product-detail-root > div.product-page-layout > div.product-details-section > div.product-details-col.col-lg-8 > div > div > div > div > div > div.glide-track > div > div:nth-child(2) > a > picture > img::attr(src)'
        ).get()
        amazon["product_image_4"] = response.css(
            'body > div.page > div.product-detail-root > div.product-page-layout > div.product-details-section > div.product-details-col.col-lg-8 > div > div > div > div > div > div.glide-track > div > div:nth-child(3) > a > picture > img::attr(src)'
        ).get()
        amazon["product_price"] = (response.css(
            "body > div.page > div.product-detail-root > div.product-page-layout > div.product-details-section > div.product-details-col.col-lg-4 > div > div.row.margin-bottom-60 > div.col-md-5 > div > div > div:nth-child(1) > div > span.sales > span::text"
        ).get() or response.css("span.sales > span::text").get())
        amazon["product_price_2"] = "null"
        amazon["product_about"] = response.css(
            "#productStorySection > div.details > div > div > ul > li::text"
        ).getall()
        amazon["product_keywords"] = response.css(
            "#productStorySection > div.details > div > li::text"
        ).getall()
        amazon["product_catlog"] = response.css(
            "body > div.page > div.product-breadcrumb > div > ul > li > a::text"
        ).getall()
        amazon["product_keywords_2"] = response.css(
            "#collapse-description > div > ul > li > span::text"
        ).getall()

        return amazon