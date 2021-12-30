#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import PepperFry


class QuotesSpider(CrawlSpider):

    name = "pepperfry"
    rotate_user_agent = True
    allowed_domains = ["www.pepperfry.com"]
    start_urls = ["https://www.pepperfry.com/"]

    rules = (Rule(sle(allow='', ), callback='parse_images', follow=True), )
   

    def parse_images(self, response):
        pepperfry = []
        pepperfry = PepperFry()
        pepperfry["product_id"] = response.css(
            "head > meta[property = 'og:url']::attr(content)"
        ).get()
        pepperfry["product_name"] = response.css(
            "#page > div.container-fluid > div.vip-product-title > h1::text"
        ).extract()
        pepperfry["product_ASIN"] = response.css(
            "#vipAddToCartButton::attr(unbxdparam_sku)"
        ).get()
        pepperfry["product_by_url"] = response.css(
            "#itemDetail > p:nth-child(2) > span[itemprop='brand']::text"
        ).get()
        pepperfry["product_by_name"] = response.css(
            "#itemDetail > p:nth-child(2) > span[itemprop='brand']::text"
        ).get()
        pepperfry["product_rating"] = response.css(
            "#page > div.container-fluid > div.vip-product-title > h1::text"
        ).get()
        pepperfry["product_image"] = response.css(
            "head > meta[property='og:image']::attr(content)"
        ).get()
        pepperfry["product_price"] = response.css(
            "#page > div.container-fluid > div.vip-pro-info.pf-white > div:nth-child(2) > div > div.pf-col.xs-12.sm-12.md-6.vip-product-content > div.vip-product-offerprize.clearfix > div > div.vipPrice > span.pf-orange-color.font-20.pf-bold-txt::text"
        ).get()
        pepperfry["product_mrp"] = response.css(
            "#page > div.container-fluid > div.vip-pro-info.pf-white > div:nth-child(2) > div > div.pf-col.xs-12.sm-12.md-6.vip-product-content > div.vip-product-offerprize.clearfix > div > div.vipPrice > span.font-16.pf-strike.pf-text-grey.pf-margin-right5::text"
        ).get()
        pepperfry["product_about"] = response.css(
            "#page > div.container-fluid > div.vip-pro-info.pf-white > div.container.pf-margin-top > div > div.row.pf-border-top.pf-medium.pf-border-right.vip-prd-dtl > div:nth-child(2) > div > div > p::text"
        ).getall()
        pepperfry["product_keywords"] = response.css(
            'head > meta[name="keywords"]::attr(content)'
        ).get()
        pepperfry["product_catlog"] = response.css(
            "#page-wrapper-content > div.breadcrumb-wrapper.pf-white > div > div > div > ul > span > li:nth-child(2) > a > span::text"
        ).getall()
        pepperfry["product_keywords_2"] = response.css("#itemDetail > p::text").getall()

        return pepperfry
