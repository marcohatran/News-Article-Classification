import scrapy 
import os
import re
from scrapy.crawler import CrawlerProcess

try:    
    from crawl_new_support import write_log, newspaper_data, createSpider, write_status
except:
    pass
try:
    from crawlData.spiders.crawl_new_support import write_log, newspaper_data, createSpider, write_status
except:
    pass

crawl_newspaper = 'vov'

class vovSpider(scrapy.Spider):
    name = 'vov'
    category = newspaper_data[crawl_newspaper][0]
    start_urls = ['https://vov.vn/' + category + '/']
    
    def cleanText(self, string):    
        noInfo = ['VOV.VN']
        for i in noInfo:
            string = string.replace(i, '')
        string = string.strip()
        return string
    
    def getContentAndSaveData(self, response, title, description):
        content = response.css("div#article-body.cms-body").css("p ::text").getall()
        content = ''.join(content)
        write_log(crawl_newspaper, self.category, title + '\n' + description + content)

    def parse(self, response):
        list_news = response.css("#aspnetForm > div.wrapper.category-page > div.body > div > div > div.col-main > section.cate-news > div.stories-style-6").css("article.story")
        for new in list_news:
            title = new.css("div.story__heading").css("a ::text").get().replace('\n', '')
            description = new.css("p.story__desc ::text").get().replace('\n', '')
            link_content = new.css(" ::attr(href)").get()
            
            if link_content is not None:
                yield scrapy.Request(
                    url=response.urljoin(link_content),
                    callback=self.getContentAndSaveData,
                    cb_kwargs={
                        'title': title,
                        'description': description
                    }
                )
        next_page = response.css("#ctl00_mainContent_ctl00_ContentListZone_pager > ul > li").css("a.next ::attr(href)").get()
        write_status(self.category, next_page)
        if next_page is not None:
            yield scrapy.Request(
                url=response.urljoin(next_page),
                callback=self.parse
            )

# # print(len(newspaper_data[crawl_newspaper]))
# createSpider(class_name='vov', newspaper_name=crawl_newspaper, 
#              nums_of_spiders = len(newspaper_data[crawl_newspaper]), 
#              url = 'https://vov.vn/', extra_url='/')

# process = CrawlerProcess()
# process.crawl(vovSpider)
# process.start()

class vovSpider1(vovSpider):
	category = newspaper_data['vov'][1]
	name = 'vov1'
	start_urls = ['https://vov.vn/' + category + '/']


class vovSpider2(vovSpider):
	category = newspaper_data['vov'][2]
	name = 'vov2'
	start_urls = ['https://vov.vn/' + category + '/']


class vovSpider3(vovSpider):
	category = newspaper_data['vov'][3]
	name = 'vov3'
	start_urls = ['https://vov.vn/' + category + '/']


class vovSpider4(vovSpider):
	category = newspaper_data['vov'][4]
	name = 'vov4'
	start_urls = ['https://vov.vn/' + category + '/']


class vovSpider5(vovSpider):
	category = newspaper_data['vov'][5]
	name = 'vov5'
	start_urls = ['https://vov.vn/' + category + '/']


class vovSpider6(vovSpider):
	category = newspaper_data['vov'][6]
	name = 'vov6'
	start_urls = ['https://vov.vn/' + category + '/']


class vovSpider7(vovSpider):
	category = newspaper_data['vov'][7]
	name = 'vov7'
	start_urls = ['https://vov.vn/' + category + '/']


class vovSpider8(vovSpider):
	category = newspaper_data['vov'][8]
	name = 'vov8'
	start_urls = ['https://vov.vn/' + category + '/']


class vovSpider9(vovSpider):
	category = newspaper_data['vov'][9]
	name = 'vov9'
	start_urls = ['https://vov.vn/' + category + '/']


class vovSpider10(vovSpider):
	category = newspaper_data['vov'][10]
	name = 'vov10'
	start_urls = ['https://vov.vn/' + category + '/']

from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
# process.crawl(vovSpider)
process.crawl(vovSpider1)
process.crawl(vovSpider2)
process.crawl(vovSpider3)
process.crawl(vovSpider4)
process.crawl(vovSpider5)
process.crawl(vovSpider6)
process.crawl(vovSpider7)
process.crawl(vovSpider8)
process.crawl(vovSpider9)
process.crawl(vovSpider10)
process.start()

# 291