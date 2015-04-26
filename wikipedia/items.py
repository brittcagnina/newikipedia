# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class NewItem(scrapy.Item):
    	title = scrapy.Field()
    	url = scrapy.Field()
    	snippet = scrapy.Field()
    	date = scrapy.Field()

class WikipediaItem(scrapy.Item):
	url = scrapy.Field()
	flag = scrapy.Field()
