# -*- coding: utf-8 -*-
import scrapy
from scrapy_pj.items import ScrapyPjItem 
import json
import re

class ApiSpider(scrapy.Spider):
    name = 'api_spider'
    def __init__(self, *args, **kwargs):
        super(ApiSpider, self).__init__(*args, **kwargs)
        self.start_url = getattr(self, 'start_url', None)
        self.start_urls = [self.start_url]
        self.allowed_domains = getattr(self, 'allowed_domains', None).split(',')
        self.keyword = getattr(self, 'keyword', None)
        self.tag = getattr(self, 'tag', None)


    def getResponseValues(self, res):
        values = []

        if type(res) is dict:
            for v in res.values():
                values.extend(self.getResponseValues(v))
        elif type(res) is list:
            for v in res:
                values.extend(self.getResponseValues(v))
        else:
            values.append(res)

        return values


    def parse(self, response):
        response = json.loads(response.body)
        values = self.getResponseValues(response)

        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )

        urls = [v for v in values if re.match(regex, str(v)) is not None]
 
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
