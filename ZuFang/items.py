# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    money = scrapy.Field()

    pass

class ZufangDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    title = scrapy.Field()
    money = scrapy.Field()
    payment = scrapy.Field()
    house_type = scrapy.Field()
    area = scrapy.Field()
    direction = scrapy.Field()
    floor = scrapy.Field()
    fitment_type = scrapy.Field()
    address = scrapy.Field()

    #title, money, payment, house_type, area, direction, floor, fitment_type, address