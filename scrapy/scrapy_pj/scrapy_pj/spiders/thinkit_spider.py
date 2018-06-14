# -*- coding: utf-8 -*-
import scrapy
from scrapy_pj.items import ScrapyPjItem 



class ThinkitSpider(scrapy.Spider):
    name = 'thinkit_spider'
    allowed_domains = ['thinkit.co.jp']
    start_urls = ['https://thinkit.co.jp']

    def parse(self, response):
        for url in response.css('a::attr("href")').extract():
            if 'article' in url:
                yield scrapy.Request('https://thinkit.co.jp' + url, self.parse_articles)

    def parse_articles(self, response):
        item = ScrapyPjItem()
        item['title'] = response.css('h1::text').extract_first()
        item['url'] = response.url
        yield item
