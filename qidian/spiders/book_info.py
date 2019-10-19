# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qidian.items import bookInfo
class BookInfoSpider(CrawlSpider):
    name = 'book_info'
    allowed_domains = ['m.qidian.com']
    start_urls = ['https://m.qidian.com/']
    custom_settings = {
        'ITEM_PIPELINES':{
            'qidian.pipelines.bookInfoPipeline':300,
        }
    }
    rules = (
        Rule(LinkExtractor(allow=r'https://m.qidian.com/book/\d+$'),callback='bookInfo_item', follow=True),
        Rule((LinkExtractor(allow=r'https://m.qidian.com/.+',deny='https://m.qidian.com/book/\d+/.+'))),
        
    )
    def bookInfo_item(self, response):
        item = bookInfo()
        item['name'] = response.xpath('//*[@id="bookDetailWrapper"]/div/div[1]/div/h2/text()').extract()[0].strip()
        item['author'] = response.xpath('//*[@id="bookDetailWrapper"]/div/div[1]/div/div[1]/a/text()').extract()[0].strip()
        item['words'] = response.xpath('//*[@id="bookDetailWrapper"]/div/div[1]/div/p[2]/text()[1]').extract()[0].strip()
        item['bclass'] = response.xpath('//*[@id="bookDetailWrapper"]/div/div[1]/div/p[1]/text()').extract()[0].strip()
        item['newz'] = response.xpath('//*[@id="ariaMuLu"]/text()[2]').extract()[0].strip()
        item['table'] = response.xpath('//*[@class="search-tags"]/a/text()').extract()   
        item['description'] = response.xpath('//*[@id="bookSummary"]/content/text()').extract()[0].strip()
        item['burl'] = response.url
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
