#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle
from ajar.items import AmazonUs


class QuotesSpider(CrawlSpider):

    name = 'amazonin'
    rotate_user_agent = True
    allowed_domains = ['www.amazon.in']
    start_urls = []

    # rules = (Rule(sle(allow='dp', deny=('product-reviews','/ap/', '/s/', '/gp/', '/hz/', '/b/','/mn/', '/slp/', '/amazonprime',)), callback='parse_images', follow=True), )

    def parse(self, response):
        amazon = []
        amazon = AmazonUs()

        amazon['product_id'] = \
            response.css('head > link[rel= "canonical"]::attr(href)').get()
        amazon['product_mrp'] = response.css('span.priceBlockStrikePriceString.a-text-strike::text').get()
        amazon['product_name'] = \
            response.css('#productTitle::text').extract()
        amazon['product_description'] = response.css('#productDescription > p::text').get()
        amazon['product_ASIN'] = \
            response.css('#averageCustomerReviews_feature_div > div#averageCustomerReviews::attr(data-asin)').get()
        amazon['product_by_url'] = \
            response.css('#bylineInfo::attr(href)').get()
        amazon['product_by_name'] = \
            response.css('#bylineInfo::text').get()
        amazon['product_rating'] = \
            response.css('#acrPopover::attr(title)').get()
        amazon['product_image'] = \
            response.css('#imgTagWrapperId > img::attr(data-old-hires)').get()
        amazon['product_image_2'] = \
            response.css('span#a-autoid-10-announce > img::attr(src)').get()
        amazon['product_image_3'] = \
            response.css('#a-autoid-11-announce > img::attr(src)').get()
        amazon['product_image_4'] = \
            response.css('#a-autoid-12-announce > img::attr(src)').get()
        amazon['product_price'] = \
            response.css('span.priceBlockBuyingPriceString::text').get()
        amazon['product_price_2'] = \
            response.css('#price_inside_buybox::text').get()
        amazon['product_about'] = \
            response.css('#feature-bullets > ul > li > span.a-list-item::text').getall()
        amazon['product_keywords'] = \
            response.css('#acBadge_feature_div > div > span.ac-for-text > span > span > a::text').get()
        amazon['product_catlog'] = \
            response.css('#wayfinding-breadcrumbs_feature_div > ul > li > span > a::text').getall()
        amazon['product_keywords_2'] = \
            response.css('#dp-container > div:nth-child(77).a-section > span:nth-child(2) > a::text').getall()
        return amazon
#  