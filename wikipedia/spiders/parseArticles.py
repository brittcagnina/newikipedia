import time
import json

from wikipedia.items import WikipediaItem

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class MySpider(BaseSpider):
    	name = "parse"
    	allowed_domains = ["wikipedia.org"]
    	start_urls = []
	needle = "different than" 
	url_count = 0;

    	def __init__(self, file, needle):
		MySpider.needle = needle
		jsonData = open(file)
		data = json.load(jsonData)
		if len(data) > 0:
			for d in data:
				MySpider.start_urls.append(d['url'])
				print d['url']
		jsonData.close()

    	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		content = hxs.select("//div[@class='mw-body']//text()").extract()
		haystack = ''.join(content) 
		if self.needle in haystack:
			wItem = WikipediaItem()
			wItem['url'] = response.url
			wItem['flag'] = MySpider.needle
			yield wItem
