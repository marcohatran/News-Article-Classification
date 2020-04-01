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

crawl_newspaper = 'laodong'

# Lao Dong
class LaoDongSpider(scrapy.Spider):
    name = "laodong"
    category = newspaper_data[crawl_newspaper][0]
    start_urls = ['https://laodong.vn/' + category + '/']
    first_page = True
    def saveData(self, response, title, description):
        content = response.css("div.left-sidebar.row > div.articleCon > div > div.wrapper-main-content > article > div.article-content ::text").getall()
        content = ''.join(content).replace('\r', '')
        content = re.sub('\n+', '\n', content).strip()
        write_log(crawl_newspaper, self.category, title + '\n' + description + content)

    def parse(self, response):

        for new in response.css("#category_main_content > ul:nth-child(1)").css("li"):
            title = new.css("h4 ::text").get()
            description = new.css("p:nth-child(4) ::text").get()
            link_content = new.css(" ::attr(href)").get()
            if link_content is not None:
                yield scrapy.Request(
                    url=link_content,
                    callback=self.saveData,
                    cb_kwargs={
                        'title': title,
                        'description': description
                    }
                )

            # find next page to crawl data
        links = response.css("#category_main_content > div > ul ::attr(href)").getall() 
        link_active = response.css("#category_main_content > div > ul > li.active ::attr(href)").get()
        if self.first_page:
            next_page = links[links.index(link_active)]
            self.first_page = False
        else:
            next_page = links[links.index(link_active) + 1]
        if next_page is not None:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse
            )

# # print(len(newspaper_data[crawl_newspaper]))
# createSpider(class_name='LaoDong', newspaper_name=crawl_newspaper, 
#              nums_of_spiders = len(newspaper_data[crawl_newspaper]), 
#              url = 'https://laodong.vn/', extra_url='/')

class LaoDongSpider1(LaoDongSpider):
	category = newspaper_data['laodong'][1]
	name = 'laodong1'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider2(LaoDongSpider):
	category = newspaper_data['laodong'][2]
	name = 'laodong2'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider3(LaoDongSpider):
	category = newspaper_data['laodong'][3]
	name = 'laodong3'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider4(LaoDongSpider):
	category = newspaper_data['laodong'][4]
	name = 'laodong4'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider5(LaoDongSpider):
	category = newspaper_data['laodong'][5]
	name = 'laodong5'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider6(LaoDongSpider):
	category = newspaper_data['laodong'][6]
	name = 'laodong6'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider7(LaoDongSpider):
	category = newspaper_data['laodong'][7]
	name = 'laodong7'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider8(LaoDongSpider):
	category = newspaper_data['laodong'][8]
	name = 'laodong8'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider9(LaoDongSpider):
	category = newspaper_data['laodong'][9]
	name = 'laodong9'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider10(LaoDongSpider):
	category = newspaper_data['laodong'][10]
	name = 'laodong10'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider11(LaoDongSpider):
	category = newspaper_data['laodong'][11]
	name = 'laodong11'
	start_urls = ['https://laodong.vn/' + category + '/']


class LaoDongSpider12(LaoDongSpider):
	category = newspaper_data['laodong'][12]
	name = 'laodong12'
	start_urls = ['https://laodong.vn/' + category + '/']


process = CrawlerProcess()
process.crawl(LaoDongSpider)
process.crawl(LaoDongSpider1)
process.crawl(LaoDongSpider2)
process.crawl(LaoDongSpider3)
process.crawl(LaoDongSpider4)
process.crawl(LaoDongSpider5)
process.crawl(LaoDongSpider6)
process.crawl(LaoDongSpider7)
process.crawl(LaoDongSpider8)
process.crawl(LaoDongSpider9)
process.crawl(LaoDongSpider10)
process.crawl(LaoDongSpider11)
process.crawl(LaoDongSpider12)
process.start()