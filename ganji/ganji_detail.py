# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time, random
from ..items import ZufangDetailItem

class GanjiDetailSpider(CrawlSpider):
    name = 'ganji_detail'
    allowed_domains = ['ganji.com']
    start_urls = ['http://sz.ganji.com/zufang/']

    rules = (
        Rule(LinkExtractor(allow=r"http://sz.ganji.com/zufang/\d+x.shtml"), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = ZufangDetailItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        time.sleep(random.random() * 3)
        item['title'] = response.xpath('.//p[@class="card-title"]/i/text()').extract()[0]
        item['money'] = response.xpath('.//span[@class="price"]/text()').extract()[0]
        item['payment'] = response.xpath('.//span[@class="unit"]/text()').extract()[0]
        item['house_type'] = response.xpath('.//div[@class="card-top"]/ul[1]/li[1]/span[2]/text()').extract()[0]
        item['area'] = response.xpath('.//div[@class="card-top"]/ul[1]/li[2]/span[2]/text()').extract()[0].replace(u'\xa0', u' ')

        item['direction'] = response.xpath('.//div[@class="card-top"]/ul[1]/li[3]/span[2]/text()').extract()[0]
        item['floor'] = response.xpath('.//div[@class="card-top"]/ul[1]/li[4]/span[2]/text()').extract()[0]
        item['fitment_type'] = response.xpath('.//div[@class="card-top"]/ul[1]/li[5]/span[2]/text()').extract()[0]
        item['address'] = response.xpath('.//div[@class="card-top"]/ul[2]/li[3]/span[2]/text()').extract()[0].replace('\n', '')
        yield item
# title, money, payment, house_type, area, direction, floor, fitment_type, address