# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class bookInfo(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field() 
    words = scrapy.Field()
    bclass = scrapy.Field()
    newz= scrapy.Field()
    table = scrapy.Field()
    description = scrapy.Field()
    burl = scrapy.Field()

