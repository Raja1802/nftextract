#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.aorg/en/latest/topics/items.html

import scrapy


# 9naime anime info downloader
class TestItem(scrapy.Item):

    name = scrapy.Field()
class gogoanimeEpisodeAPI(scrapy.Item):
    ep_url = scrapy.Field()
    episode_name = scrapy.Field()
    cate = scrapy.Field()
    vien = scrapy.Field()
    uri = scrapy.Field()

class gogoanimeEpisode(scrapy.Item):
    ep_url = scrapy.Field()
    anime_id = scrapy.Field()
    name = scrapy.Field()
    server_1 = scrapy.Field()
    server_2 = scrapy.Field()
    server_3 = scrapy.Field()
    server_4 = scrapy.Field()
    server_5 = scrapy.Field()
    server_6 = scrapy.Field()
    server_7 = scrapy.Field()
    server_8 = scrapy.Field()
    server_9 = scrapy.Field()
    server_10 = scrapy.Field()
    server_11 = scrapy.Field()
    server_12 = scrapy.Field()

class gogoanimeAnime(scrapy.Item):
    anime_id = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    season_type = scrapy.Field()
    plot_summary = scrapy.Field()
    genre = scrapy.Field()
    released = scrapy.Field()
    status = scrapy.Field()
    total_episodes = scrapy.Field()
    other_names = scrapy.Field()


class AjarItem(scrapy.Item):

    name = scrapy.Field()
    image = scrapy.Field()
    synonyms = scrapy.Field()
    types = scrapy.Field()
    studios = scrapy.Field()
    aired = scrapy.Field()
    status = scrapy.Field()
    scores = scrapy.Field()
    premired = scrapy.Field()
    durination = scrapy.Field()
    quality = scrapy.Field()
    gener = scrapy.Field()
    about = scrapy.Field()
    tags = scrapy.Field()
    cover = scrapy.Field()


class AmazonUs(scrapy.Item):
    product_id = scrapy.Field()
    product_mrp = scrapy.Field()
    product_description = scrapy.Field()
    product_name = scrapy.Field()
    product_ASIN = scrapy.Field()
    product_by_url = scrapy.Field()
    product_by_name = scrapy.Field()
    product_rating = scrapy.Field()
    product_image = scrapy.Field()
    product_image_2 = scrapy.Field()
    product_image_3 = scrapy.Field()
    product_image_4 = scrapy.Field()
    product_price = scrapy.Field()
    product_about = scrapy.Field()
    product_keywords = scrapy.Field()
    product_catlog = scrapy.Field()
    product_price_2 = scrapy.Field()
    product_keywords_2 = scrapy.Field()


class PepperFry(scrapy.Item):
    product_id = scrapy.Field()
    product_name = scrapy.Field()
    product_ASIN = scrapy.Field()
    product_by_url = scrapy.Field()
    product_by_name = scrapy.Field()
    product_rating = scrapy.Field()
    product_image = scrapy.Field()
    product_price = scrapy.Field()
    product_about = scrapy.Field()
    product_keywords = scrapy.Field()
    product_catlog = scrapy.Field()
    product_mrp = scrapy.Field()
    product_keywords_2 = scrapy.Field()


class AmazonPerfect(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    colour = scrapy.Field()
    instock = scrapy.Field()
    reviews = scrapy.Field()
    description = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    keywords = scrapy.Field()


class UnsplashApi(scrapy.Item):
    img_id = scrapy.Field()
    alt_description = scrapy.Field()
    categories = scrapy.Field()
    color = scrapy.Field()
    created_at = scrapy.Field()
    current_user_collections = scrapy.Field()
    description = scrapy.Field()
    height = scrapy.Field()
    width = scrapy.Field()
    links_download = scrapy.Field()
    links_download_location = scrapy.Field()
    links_html = scrapy.Field()
    links_self = scrapy.Field()
    urls_full = scrapy.Field()
    urls_raw = scrapy.Field()
    urls_regular = scrapy.Field()
    urls_small = scrapy.Field()
    urls_thumb = scrapy.Field()
    updated_at = scrapy.Field()


class Myanimelist(scrapy.Item):
    anime_name = scrapy.Field()
    anime_discription = scrapy.Field()
    anime_name_english = scrapy.Field()
    anime_name_japanese = scrapy.Field()
    anime_type = scrapy.Field()
    anime_episodes = scrapy.Field()
    anime_status = scrapy.Field()
    anime_aired = scrapy.Field()
    anime_primered = scrapy.Field()
    anime_broadcast = scrapy.Field()
    anime_producers = scrapy.Field()
    anime_licence = scrapy.Field()
    anime_studios = scrapy.Field()
    anime_source = scrapy.Field()
    anime_gener = scrapy.Field()
    anime_durination = scrapy.Field()
    anime_rating = scrapy.Field()
    anime_score = scrapy.Field()
    anime_popularity = scrapy.Field()
    anime_season = scrapy.Field()
    anime_trailer = scrapy.Field() 


class Shopstyles(scrapy.Item):
    url = scrapy.Field()
    response = scrapy.Field()

class ProxyServerData(scrapy.Item):
    proxy = scrapy.Field()

class LinkExtracters(scrapy.Item):
    url = scrapy.Field()
    website = scrapy.Field()

class UrlExtracters(scrapy.Item):
    url = scrapy.Field()
    canonical = scrapy.Field()
    website = scrapy.Field()

class SpecsExtractor(scrapy.Item):
    pid = scrapy.Field()
    specKey = scrapy.Field()
    specValue =scrapy.Field()

class ImageExtractor(scrapy.Item):
    pid = scrapy.Field()
    image = scrapy.Field()

class PriceExtractor(scrapy.Item):
    pid = scrapy.Field()
    price_mrp = scrapy.Field()
    price = scrapy.Field()
    price_2 = scrapy.Field()
    
class SpecImage(scrapy.Item):
    images = scrapy.Field()
    specs = scrapy.Field()