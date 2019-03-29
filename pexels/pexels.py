# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ImagesItem


class PexelsSpider(CrawlSpider):
    name = 'pexels'
    allowed_domains = ['pexels.com']
    start_urls = ['https://www.pexels.com']

    rules = (
        Rule(LinkExtractor(allow=r'^https://www.pexels.com/photo/.*/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ImagesItem()
        item['image_urls'] = response.xpath('.//a[@class="js-photo-link photo-item__link"]/img/@src').extract()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print(item)
        return item
