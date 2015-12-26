import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Crxdy(CrawlSpider):
	name = 'cl1024'
	allowed_domains = ['cl.weod.pw']
	start_urls = ['http://cl.weod.pw/thread0806.php?fid=22&search=&page=1']
	rules = (
		Rule(LinkExtractor(allow='thread0806\.php\?fid=22&search=&page=(\d+)'), 'parse_list', follow=True,),
	)
	
	def parse_list(self, response):
		self.logger.info('Hi, this is an list page %s', response.url)
		#title  response.xpath('//tr/td/h3/a/text()')
		#href  response.xpath('//tr/td/h3/a/@href') 
		#data storage nesting and export to csv 
		item = scrapy.Item()
		