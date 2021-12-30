#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(CrawlSpider):

    name = "mintb"
    rotate_user_agent = True
    allowed_domains = ["www.nike.com"]
    start_urls = ["https://www.nike.com/"]

    rules = (Rule(sle(allow="/in/t/",), callback="parse_images", follow=True,),)

    def parse_images(self, response):
        amazon = []
        amazon = AmazonUs()

        amazon["product_id"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_mrp"] = response.css(
            "#RightRail > div > div.css-1ne55sl.mb2-sm > div > div.d-lg-ib.mb0-sm.u-full-width.css-74mc45 > div.headline-5.ta-sm-r.css-1122yjz > div > div::text"
        ).get()
        amazon["product_name"] = response.css("#pdp_product_title::text").get()
        amazon["product_description"] = response.css(
            "#RightRail > div > div.pt4-sm.prl6-sm.prl0-lg > div.description-preview.body-2.css-1pbvugb > p::text"
        ).get()
        amazon["product_ASIN"] = response.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        amazon["product_by_url"] = "nike.com"
        amazon["product_by_name"] = "nike"
        amazon["product_rating"] = response.css(
            "#RightRail > div > div.mt3-sm.pt12-sm.pt10-lg.mt0-lg.border-bottom.mr6-sm.ml6-sm.mr0-lg.ml0-lg.css-1xydj8n.css-bxtnul > div:nth-child(2) > button > div.ncss-col-sm-7.css-17y0hnb > h3::text"
        ).get()
        amazon["product_image"] = response.css(
            "head > meta[property='og:image']::attr(content)"
        ).get()
        amazon["product_price"] = response.css(
            "#RightRail > div > div.css-1ne55sl.mb2-sm > div > div.d-lg-ib.mb0-sm.u-full-width.css-74mc45 > div.headline-5.ta-sm-r.css-1122yjz > div > div::text"
        ).get()
        amazon["product_price_2"] = response.css(
            "#RightRail > div > div.css-1ne55sl.mb2-sm > div > div.d-lg-ib.mb0-sm.u-full-width.css-74mc45 > div.headline-5.ta-sm-r.css-1122yjz > div > div::text"
        ).get()
        amazon["product_about"] = response.css(
            "#RightRail > div > div.pt4-sm.prl6-sm.prl0-lg > div.css-1waa9ub.popup-drawer.z9.show > div.ncss-container.ncss-col-sm-12.css-ssux7 > div > div > div > p::text"
        ).getall()
        amazon["product_keywords"] = response.css(
            "#RightRail > div > div.pt4-sm.prl6-sm.prl0-lg > div.css-1waa9ub.popup-drawer.z9.show > div.ncss-container.ncss-col-sm-12.css-ssux7 > div > div > div > ul > li::text"
        ).getall()
        amazon["product_catlog"] = (
            response.css("head > meta[name='keywords']::attr(content)").getall()
            + response.css("head > meta[name='description']::attr(content)").getall()
        )
        amazon["product_keywords_2"] = response.css(
            "#RightRail > div > div.pt4-sm.prl6-sm.prl0-lg > div.css-1waa9ub.popup-drawer.z9.show > div.ncss-container.ncss-col-sm-12.css-ssux7 > div > div > div > ul:nth-child(18) > li::text"
        ).getall()

        return amazon
