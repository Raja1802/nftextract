#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(CrawlSpider):

    name = 'nykaa'
    rotate_user_agent = True
    allowed_domains = ['www.nykaa.com']
    start_urls = []

    #rules = (Rule(sle(allow='p', deny=("/c/")), callback='parse_images', follow=True), )

    def parse(self, response):
        amazon = []
        amazon = AmazonUs()

        amazon['product_id'] = \
            response.css('head > link[rel= "canonical"]::attr(href)').get()
        amazon['product_mrp'] = response.css('span.mrp-price::text').getall()
        amazon['product_name'] = \
            response.css('h1.product-title::text').extract()
        amazon['product_description'] = response.css('div.A-PlusContent::text').get()
        amazon['product_ASIN'] = \
            response.css('head > link[rel= "canonical"]::attr(href)').get()
        amazon['product_by_url'] = "nykaa.com"
        amazon['product_by_name'] = "nykaa"
        amazon['product_rating'] = \
            response.css('div.rating-count-popup__rating-count::text').get()
        amazon['product_image'] = \
            response.css('#carousel-bounding-box > div.pd-main-image > div > div > div > img::attr(src)').get()
        amazon['product_image_2'] = \
            response.css('#carousel-bounding-box > div.slick-thumb > div > div > div > div.slick-slide[data-index="2"] > div > img::attr(src)').get()
        amazon['product_image_3'] = \
            response.css('#carousel-bounding-box > div.slick-thumb > div > div > div > div.slick-slide[data-index="3"] > div > img::attr(src)').get()
        amazon['product_image_4'] = \
            response.css('#carousel-bounding-box > div.slick-thumb > div > div > div > div.slick-slide[data-index="4"] > div > img::attr(src)').get()
        amazon['product_price'] = \
            response.css('span.post-card__content-price-offer::text').getall()
        amazon['product_price_2'] = \
            response.css('span.post-card__offers-offer::text').getall()
        amazon['product_about'] = \
            response.css('#color-section > div.clearfix > div > div > div > select > option::text').getall()
        amazon['product_keywords'] = \
            response.css('div.pdp-description-tab-item  > div > p::text').getall()
        amazon['product_catlog'] = \
            response.css('div.container > div.clearfix > div > ol.breadcrumb > li > a::text').getall()
        amazon['product_keywords_2'] = \
            response.css('head > meta[name="description"]::attr(content)').getall()
        return amazon
#  