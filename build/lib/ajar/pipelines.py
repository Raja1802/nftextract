# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import urllib


class AjarPipeline:
    # def __init__(self):
    #     self.conn = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@scraper0-shard-00-00-vtwhx.mongodb.net:27017,scraper0-shard-00-01-vtwhx.mongodb.net:27017,scraper0-shard-00-02-vtwhx.mongodb.net:27017/ajar?ssl=true&replicaSet=Scraper0-shard-0&authSource=admin&retryWrites=true&w=majority")
    #     db = self.conn.ajar
    #     self.collection = db.ajar
    def process_item(self, item, spider):
        # client = pymongo.MongoClient(
        #     "mongodb://ajar:"
        #     + urllib.parse.quote_plus("Raja@1802")
        #     + "@cluster0-shard-00-00.rqssk.mongodb.net:27017,cluster0-shard-00-01.rqssk.mongodb.net:27017,cluster0-shard-00-02.rqssk.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-6w1hgf-shard-0&authSource=admin&retryWrites=true&w=majority"
        # )
        # client = pymongo.MongoClient("mongodb+srv://ajar:"+ urllib.parse.quote_plus("Raja@1802")+ "@cluster0.rqssk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        # mongodb+srv://ajar:<password>
        # print(self)
        client = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@cluster0-shard-00-00.eyv0d.mongodb.net:27017,cluster0-shard-00-01.eyv0d.mongodb.net:27017,cluster0-shard-00-02.eyv0d.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-110jin-shard-0&authSource=admin&retryWrites=true&w=majority")
        db = client.testing_Api
        collect = db.reliace_prices
        collect_price = db.prices
        print(item)
        # collect.insert(dict(item))#
        # {'pid':item['pid'],"specKey": item["specKey"]}specValue
        if "specValue" in item:
            dup_check = collect.find({'pid':item['pid'],"specValue": item["specValue"]}).count()
            if dup_check == 0 :     
                collect.insert(dict(item))
                print ("product Added!")
            else:
                print("product Exist")
            return item
        elif "price" in item:
            dup_check = collect_price.find({'pid':item['pid']}).count()
            if dup_check == 0 :     
                collect_price.insert(dict(item))
                print ("price Added!")
            else:
                print("price Exist")
            return item
        # client.close()#
        
        # collect.insert(dict(item))
        # self.collection.insert(dict(item))
        # return item
