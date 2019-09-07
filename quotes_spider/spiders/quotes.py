# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        item_loader = ItemLoader(item=QuotesSpiderItem(), response=response)
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tags-item"]/a/text()').extract()
        item_loader.add_value('h1_tag', h1_tag)
        item_loader.add_value('tags', tags)

        return item_loader.load_item()

