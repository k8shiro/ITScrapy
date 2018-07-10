# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from time import sleep
import requests
import json
import os

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

    def post_slack(self, item):
        url = os.environ["SLACK_WEBHOOK"]
        print(url)
        if url != "":
            data = json.dumps({
                'text':  item['title'] + '\n'+ item['url'],
                'unfurl_links': 'true'
            })

            response = requests.post(url, data=data)
            print(response.text)

    def post_mattermost(self, item):
        url = os.environ["MATTERMOST_WEBHOOK"]
        if url != "":
            data = json.dumps({
                'text':  item['title'] + '\n'+ item['url'],
                'unfurl_links': 'true'
            })

            response = requests.post(url, data=data)
            print(response.text)

    def process_item(self, item, spider):
        is_saved = self.db['clip'].update(
            {u'url': item['url']},
            {"$set": dict(item)},
            upsert = True
        ) # linkを検索して、なければ新規作成、あればアップデートする

        is_saved = is_saved['updatedExisting']

        print("--------------------------")
        print("title: {}".format(item['title']))
        # is_saved=Falseで新規
        print("is_saved: {}".format(is_saved))
        print("--------------------------")

        if is_saved == False:
            self.post_slack(item)
            self.post_mattermost(item)

        sleep(12)

        return item
