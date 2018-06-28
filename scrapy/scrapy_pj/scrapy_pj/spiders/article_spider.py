# -*- coding: utf-8 -*-
import scrapy
from scrapy_pj.items import ScrapyPjItem 



class ArticleSpider(scrapy.Spider):
    name = 'article_spider'
    def __init__(self, *args, **kwargs):
        super(ArticleSpider, self).__init__(*args, **kwargs)
        self.start_url = getattr(self, 'start_url', None)
        self.start_urls = [self.start_url]
        self.allowed_domains = getattr(self, 'allowed_domains', None).split(',')
        self.keyword = getattr(self, 'keyword', None)
        self.tag = getattr(self, 'tag', None)

    def parse(self, response):
        for url in response.css('a::attr("href")').extract():
            if 'http' in url and not self.start_url in url:
                continue
            if not 'http' in url:
                url = response.urljoin(url)
            if self.keyword in url:
                yield scrapy.Request(url, self.parse_articles)

    def parse_articles(self, response):
        item = ScrapyPjItem()
        item['img'] = response.css('meta[property="og:image"]::attr(content)').extract_first()
        item['title'] = response.css('title::text').extract_first()
        item['url'] = response.url
        item['tag'] = self.tag
        yield item
