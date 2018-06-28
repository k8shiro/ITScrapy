# -*- coding: utf-8 -*-
import scrapy
from scrapy_pj.items import ScrapyPjItem 



class ThinkitSpider(scrapy.Spider):
    name = 'thinkit_spider'
    def __init__(self, *args, **kwargs):
        super(ThinkitSpider, self).__init__(*args, **kwargs)

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(getattr(self, 'start_urls', None))
        self.start_urls = getattr(self, 'start_urls', None).split(',')
        self.allowed_domains = getattr(self, 'allowed_domains', None).split(',')
        self.keyword = getattr(self, 'keyword', None)

    #allowed_domains = ['thinkit.co.jp']
    #start_urls = ['https://thinkit.co.jp']

    def parse(self, response):
        for url in response.css('a::attr("href")').extract():
            if "http" not in url and self.keyword in url:
                yield scrapy.Request('https://thinkit.co.jp' + url, self.parse_articles)

    def parse_articles(self, response):
        item = ScrapyPjItem()
        item['title'] = response.css('h1::text').extract_first()
        item['url'] = response.url
        yield item
