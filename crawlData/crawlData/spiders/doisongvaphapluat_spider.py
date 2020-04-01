import scrapy 
import os
import re
from scrapy.crawler import CrawlerProcess

try:    
    from crawl_new_support import write_log, newspaper_data, createSpider
except:
    pass
try:
    from crawlData.spiders.crawl_new_support import write_log, newspaper_data, createSpider
except:
    pass

crawl_newspaper = 'doisongvaphapluat'

class DoiSongVaPhapLuatSpider(scrapy.Spider):
    name ="doisongvaphapluat"
    start_urls = ['https://www.doisongphapluat.com/' + sub_page + '/' for sub_page in newspaper_data[name]]

    def cleanText(self, string):    
        noInfo = ['NDĐT', '[Infographic]']
        for i in noInfo:
            string = string.replace(i, '')
        string = string.strip()
        return string

    def parse(self, response):
        category = str(response.url).replace('https://www.doisongphapluat.com/', '').replace('/', '').replace('.htm', '')
        list_news = response.css('ul.module-vertical-list')
        for new in list_news.css('li'):
            # ignore advertisements
            if new.css('label._mB::text').get() == 'QC':
                pass
            else:
                # get titles
                title = new.css('h4.title ::text').getall()
                title = ''.join(title)
                write_log(self.name, category, self.cleanText(title))

                # get summary
                des = new.css('p.desc ::text').getall()
                des = ''.join(des)
                write_log(self.name, category, self.cleanText(des))

process = CrawlerProcess()
process.crawl(DoiSongVaPhapLuatSpider)
process.start()