import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Crxdy(CrawlSpider):
	name = 'tech.163'
	allowed.domains = ['tech.163.com']
	start_urls = ['http://tech.163.com/special/0009rt/tech_it.html']
	rules = (
		Rule
	)