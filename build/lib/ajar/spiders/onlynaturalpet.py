#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(CrawlSpider):

    name = "onlynaturalpet"
    rotate_user_agent = True
    allowed_domains = ["www.onlynaturalpet.com"]
    start_urls = ["https://www.onlynaturalpet.com/"]

    rules = (Rule(sle(allow="products",), callback="parse_images", follow=True,),)

    def parse_images(self, response):
        amazon = []
        amazon = AmazonUs()

        amazon["product_id"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_mrp"] = response.css(
            " div.product-price-wrapper > span.u-td-strike::text"
        ).getall()
        amazon["product_name"] = response.css(" h1.product-title::text").get()
        amazon["product_description"] = response.css(
            "div.product-description > p::text"
        ).get()
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "onlynaturalpet.com"
        amazon["product_by_name"] = "onlynaturalpet"
        amazon["product_rating"] = response.css(
            "#shopify-section-product > div > div > div:nth-child(7) > div > div.row > div.col-md-7.col-lg-6 > div > div.hidden-sm.hidden-xs > div.product-info-widget-container > div > span > div.standalone-bottomline > div.yotpo-bottomline.pull-left.star-clickable > a::text"
        ).getall()
        amazon["product_image"] = (
            response.css("li.product-gallery__slideshow-slide > a::attr(href)").get()
            or response.css("head > meta[property='og:image']::attr(content)").get()
        )
        amazon["product_price"] = (
            response.css(
                " div.product-price-wrapper > span.u-color-onp-green-alt.u-fs-medium.u-fw-medium::text"
            ).getall()
            or response.css("div.product-price-wrapper > span::text").get()
        )
        amazon["product_price_2"] = response.css(
            " div.product-price-wrapper > span.u-fs-medium.u-fw-medium::text"
        ).getall()
        amazon["product_about"] = response.css(
            "div.product-description > div >p::text"
        ).getall()
        amazon["product_keywords"] = response.css(
            "div#list-rich-text-product > ul > li::text"
        ).getall()
        amazon["product_catlog"] = response.css(
            "div.breadcrumbs__crumb > a::text"
        ).getall()
        amazon["product_keywords_2"] = response.css(
            "head > meta[property='og:description']::attr(content)"
        ).getall()

        return amazon
