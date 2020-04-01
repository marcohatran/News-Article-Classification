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

crawl_newspaper = 'nhandan'

# Nhan Dan
class NhanDanSpider(scrapy.Spider):
    name = "nhandan"
    category = newspaper_data[crawl_newspaper][0]
    start_urls = ['https://nhandan.com.vn/' + category]

    # Clean the text 
    def cleanText(self, string):    
        noInfo = ['NDĐT', '–', '-', '[Infographic]', '*']
        for i in noInfo:
            string = string.replace(i, '')
        string = re.sub('  +', '', string)
        return string

    def getContentAndSaveData(self, response, title, description):
        content = response.css("#wrapper > div.container.plr-0.content-container > div.item-wrapper > div > div > div:nth-child(1) > div > div.item-content ::text").getall()
        content = ''.join(content)
        content = re.sub('\n+', '', content)
        description = self.cleanText(description)
        write_log(crawl_newspaper, self.category, title + '\n'+ description + content)

    def parse(self, response):
        # title 
        list_news = response.css("#wrapper > div.container.plr-0.content-container > div.row.pt-20 > div:nth-child(2) > div:nth-child(1) > div.hotnew-container.lop3").css("div.media.content-box")
        for new in list_news:
            # title
            title = new.css("h5.mt-0").css("a ::text").get()
            
            # description
            description = new.css("p ::text").get()
            
            # link 
            link_content = new.css("div.media-body ::attr(href)").get()

            if link_content is not None:
                yield scrapy.Request(
                    url=response.urljoin(link_content),
                    callback=self.getContentAndSaveData,
                    cb_kwargs={
                        'title': title,
                        'description': description
                    }
                )
        next_page = response.css("#wrapper > div.container.plr-0.content-container > div.row.pt-20 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div > div > ul ::attr(href)").getall()[-1]
        if next_page is not None:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse
            )

# # print(len(newspaper_data[crawl_newspaper]))
# createSpider(class_name='NhanDan', newspaper_name=crawl_newspaper, 
#              nums_of_spiders = len(newspaper_data[crawl_newspaper]), 
#              url = 'https://nhandan.com.vn/', extra_url='')

class NhanDanSpider1(NhanDanSpider):
	category = newspaper_data['nhandan'][1]
	name = 'nhandan1'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider2(NhanDanSpider):
	category = newspaper_data['nhandan'][2]
	name = 'nhandan2'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider3(NhanDanSpider):
	category = newspaper_data['nhandan'][3]
	name = 'nhandan3'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider4(NhanDanSpider):
	category = newspaper_data['nhandan'][4]
	name = 'nhandan4'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider5(NhanDanSpider):
	category = newspaper_data['nhandan'][5]
	name = 'nhandan5'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider6(NhanDanSpider):
	category = newspaper_data['nhandan'][6]
	name = 'nhandan6'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider7(NhanDanSpider):
	category = newspaper_data['nhandan'][7]
	name = 'nhandan7'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider8(NhanDanSpider):
	category = newspaper_data['nhandan'][8]
	name = 'nhandan8'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider9(NhanDanSpider):
	category = newspaper_data['nhandan'][9]
	name = 'nhandan9'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider10(NhanDanSpider):
	category = newspaper_data['nhandan'][10]
	name = 'nhandan10'
	start_urls = ['https://nhandan.com.vn/' + category + '']


class NhanDanSpider11(NhanDanSpider):
	category = newspaper_data['nhandan'][11]
	name = 'nhandan11'
	start_urls = ['https://nhandan.com.vn/' + category + '']


process = CrawlerProcess()
process.crawl(NhanDanSpider)
process.crawl(NhanDanSpider1)
process.crawl(NhanDanSpider2)
process.crawl(NhanDanSpider3)
process.crawl(NhanDanSpider4)
process.crawl(NhanDanSpider5)
process.crawl(NhanDanSpider6)
process.crawl(NhanDanSpider7)
process.crawl(NhanDanSpider8)
process.crawl(NhanDanSpider9)
process.crawl(NhanDanSpider10)
process.crawl(NhanDanSpider11)
process.start()