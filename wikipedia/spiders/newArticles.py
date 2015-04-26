import time
from wikipedia.items import NewItem

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from selenium import webdriver 


class MySpider(BaseSpider):
    	name = "new"
    	allowed_domains = ["wikipedia.org"]
    	start_urls = ["https://en.wikipedia.org/wiki/Special:NewPagesFeed"]

    	def __init__(self):
		self.driver = webdriver.Firefox()

    	def parse(self, response):
		self.driver.get(response.url)
		time.sleep(3)

 		items = self.driver.find_elements_by_class_name("mwe-pt-list-item")
		for item in items:
			#print item.get_attribute('innerHTML')

			title = item.find_element_by_class_name('mwe-pt-page-title')
			url = title.find_element_by_tag_name('a')
			snippet = item.find_element_by_class_name('mwe-pt-snippet')
			date = item.find_element_by_class_name('mwe-pt-creation-date')
			
			nItem = NewItem()
			nItem['title'] = title.text
			nItem['url'] = url.get_attribute('href')
			nItem['snippet'] = snippet.text
			nItem['date'] = date.text
			yield nItem

		self.driver.close()
