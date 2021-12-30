#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(SitemapSpider):
    name = "backcountry"
    rotate_user_agent = True
    allowed_domains = ["www.backcountry.com"]
    # start_urls = ["https://www.backcountry.com/"]
    sitemap_urls = ["https://www.backcountry.com/productSitemap.xml"]

    # rules = (Rule(sle(allow="",), callback="parse_images", follow=True,),)

    def parse(self, response):
        amazon = []
        amazon = AmazonUs()

        amazon["product_id"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_mrp"] = response.css(
            "#content > div > div.product-overview.js-product-overview > section.product-buybox.js-product-buybox.qa-product-buybox > div.product-pricing.js-item-price > span.product-pricing__inactive::text"
        ).getall()
        amazon["product_name"] = (
            response.css("h1.product-name::text").getall()
            or response.css("head > meta[property='og:title']::attr(content)").get()
        )
        amazon["product_description"] = response.css(
            "#product_info > div.ui-product-details__description::text"
        ).getall()
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "backcountry.com"
        amazon["product_by_name"] = "backcountry"
        amazon["product_rating"] = (
            response.css(
                "span.product-details__community-rating rating > span::text"
            ).getall()
            or "NULL"
        )
        amazon["product_image"] = (
            response.css("img.ui-flexslider__img::attr(data-src-zoomin)").get()
            or response.css("head > meta[property='og:image']::attr(content)").get()
        )
        amazon["product_price"] = (
            response.css(
                "#content > div > div.product-overview.js-product-overview > section.product-buybox.js-product-buybox.qa-product-buybox > div.product-pricing.js-item-price > span.product-pricing__sale::text"
            ).getall()
            or response.css(
                "#content > div > div.product-overview.js-product-overview > section.product-buybox.js-product-buybox.qa-product-buybox > div.product-pricing.js-item-price > span.product-pricing__retail::text"
            ).getall()
        )
        amazon["product_price_2"] = response.css(
            "#content > div > div.product-overview.js-product-overview > section.product-buybox.js-product-buybox.qa-product-buybox > div.product-pricing.js-item-price > div.product-pricing__discount::text"
        ).getall()
        amazon["product_about"] = response.css("#product_info > ul > li::text").getall()
        amazon["product_keywords"] = response.css(
            "#product_info > div.product-details__techspecs.js-product-details-techspecs.qa-product-details-techspecs > dl.product-details__techspecs-list.product-details__first-column.js-techspecs-first-column > div > dd::text"
        ).getall()
        amazon["product_catlog"] = response.css("a.qa-breadcrumb-link::text").getall()
        amazon["product_keywords_2"] = response.css(
            "head > meta[property='og:description']::attr(content)"
        ).getall()

        return amazon
