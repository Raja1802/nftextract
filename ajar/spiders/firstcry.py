#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(CrawlSpider):

    name = 'fcry'
    rotate_user_agent = True
    allowed_domains = ['www.firstcry.com']
    start_urls = ['https://www.firstcry.com/']

    rules = (Rule(sle(allow='',), callback='parse_images', follow=True), )

    def parse_images(self, response):
        amazon = []
        amazon = AmazonUs()


        amazon['product_id'] = \
            response.css('head > link[rel= "canonical"]::attr(href)').get()
        amazon['product_mrp'] = response.css('#original_mrp::text').getall()
        amazon['product_name'] = \
            (response.css('#prod_name::text').get()
            or
            response.css("#prod_name::text").getall())
        amazon['product_description'] = response.css('#div_prod_desc > div > span:nth-child(3)::text').getall()
        amazon['product_ASIN'] = response.css('head > link[rel= "canonical"]::attr(href)').get()
        amazon['product_by_url'] = "firstcry.com"
        amazon['product_by_name'] = "firstcry"
        amazon['product_rating'] = "NAN"
        amazon['product_image'] = \
            response.css('#big-img::attr(src)').get()
        amazon['product_image_2'] = \
            response.css('#slide-wrap > div > img[data-id="2"]::attr(src)').get()
        amazon['product_image_3'] = \
            response.css('#slide-wrap > div > img[data-id="3"]::attr(src)').get()
        amazon['product_image_4'] = \
            response.css('#slide-wrap > div > img[data-id="4"]::attr(src)').get()
        amazon['product_price'] = \
            response.css('#prod_price::text').get()
        amazon['product_price_2'] = \
            response.css('#prod_discount::text').get()
        amazon['product_about'] = \
            response.css('#p_breadcrumb > div.pdp-wrap > div > div.baby-gear-wrap.clearfix > div.right-contr > div.prod-info-wrap > div.div-chk-delivery.clearfix > div.div-kh.clearfix > div.div-brand-info > div.p_bi_dtl_sct.p_lft.pw > div::text').getall()
        amazon['product_keywords'] = \
            response.css('div.div-snf-info > p > span::text').getall()
        amazon['product_catlog'] = \
            response.css('#p_breadcrumb > div.pdp-wrap > div > div.breadcrumb > a::text').getall()
        amazon['product_keywords_2'] = \
            response.css('head > meta[name="keywords"]::attr(content)').getall()

        return amazon
#  