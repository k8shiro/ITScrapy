# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class ScrapyPjPipeline(object):
    def __init__(self):
        # インスタンス生成時に渡された引数で、変数初期化
        self.mongo_uri = "mongo"
        self.mongo_db = "scrapy"
        self.mongo_user = "mongoadmin"
        self.mongo_pass = "password"

    def open_spider(self, spider): # スパイダー開始時に実行される。データベース接続
        self.client = MongoClient(self.mongo_uri)
        self.client['admin'].authenticate(self.mongo_user, self.mongo_pass)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider): # スパイダー終了時に実行される。データベース接続を閉じる
        self.client.close()

    def process_item(self, item, spider):
        is_save = self.db['article'].update(
            {u'url': item['url']},
            {"$set": dict(item)},
            upsert = True
        ) # linkを検索して、なければ新規作成、あればアップデートする

        print("is_save:@@@@@@@@@@")
        print(is_save)
        print("is_save:*************")
        return item
