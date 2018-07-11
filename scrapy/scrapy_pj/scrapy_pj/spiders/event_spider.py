# -*- coding: utf-8 -*-
import scrapy
from scrapy_pj.items import ScrapyPjItem 
import json
import re
import dpath.util

class EventSpider(scrapy.Spider):
    name = 'event_spider'
    def __init__(self, *args, **kwargs):
        super(EventSpider, self).__init__(*args, **kwargs)
        self.start_url = getattr(self, 'start_url', None)
        self.start_urls = [self.start_url]
        self.allowed_domains = getattr(self, 'allowed_domains', None).split(',')
        self.keyword = getattr(self, 'keyword', None)
        self.events_key = getattr(self, 'events_key', None)
        self.limit_key = getattr(self, 'limit_key', None)
        self.url_key = getattr(self, 'url_key', None)
        self.tag = getattr(self, 'tag', None)


    def parse(self, response):
        events = json.loads(response.body)
 
        if self.events_key is not None:
            events = dpath.util.get(events, self.events_key)

        urls = []
        if self.limit_key is not None:
            limit_key = self.limit_key
            for event in events:
                limit = dpath.util.get(event, self.limit_key)
                if limit is not None and limit >=40:
                    url = dpath.util.get(event, self.url_key)
                    urls.append(url)
 
        for url in urls:
             if self.keyword in url:
                 yield scrapy.Request(url, self.parse_articles)


    def parse_articles(self, response):
        item = ScrapyPjItem()
        item['img'] = response.css('meta[property="og:image"]::attr(content)').extract_first()
        item['title'] = response.css('title::text').extract_first()
        item['url'] = response.url
        item['tag'] = self.tag
        yield item
