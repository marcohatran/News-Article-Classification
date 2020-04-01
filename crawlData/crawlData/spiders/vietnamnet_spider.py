import scrapy 
import os
import re
import json
try:    
    from crawl_new_support import write_log, newspaper_data, createSpider
except:
    pass
try:
    from crawlData.spiders.crawl_new_support import write_log, newspaper_data, createSpider
except:
    pass
from scrapy.crawler import CrawlerProcess

crawl_newspaper = 'vietnamnet'

# VietNamNet
class VietNamNetSpider(scrapy.Spider):
    name = "vietnamnet"
    category = newspaper_data[crawl_newspaper][0]
    
    # start_urls = ['https://vietnamnet.vn/vn/' + sub_page + '/trang%d/' %i for sub_page in newspaper_data[name] for i in range(1, 5)]
    start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]
    page_count = 1

    def getContentAndSaveData(self, response, title, description):
        content = response.css("#ArticleContent").css("p ::text").getall()
        content = ''.join(content)
        write_log(crawl_newspaper, self.category, title + '\n' + description + content)

    def parse(self, response):
        
        list_news = json.loads(response.css(" ::text").get()[8:])
        for new in list_news:
            title = new['title']
            description = new['lead']
            link_content = new['link']
            if link_content is not None:
                yield scrapy.Request(
                    url = link_content,
                    callback=self.getContentAndSaveData,
                    cb_kwargs={
                        'title': title,
                        'description': description
                    }
                )

        self.page_count += 1
        next_page = 'https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p={}&s=15&a=5'.format(self.category, self.page_count)
        yield scrapy.Request(
            url = next_page, 
            callback= self.parse
        )

# print(len(newspaper_data[crawl_newspaper]))
createSpider(class_name='VietNamNet', newspaper_name=crawl_newspaper, 
             nums_of_spiders = len(newspaper_data[crawl_newspaper]), 
             url = "https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)")        
    
class VietNamNetSpider1(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][1]
	name = 'vietnamnet1'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider2(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][2]
	name = 'vietnamnet2'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider3(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][3]
	name = 'vietnamnet3'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider4(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][4]
	name = 'vietnamnet4'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider5(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][5]
	name = 'vietnamnet5'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider6(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][6]
	name = 'vietnamnet6'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider7(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][7]
	name = 'vietnamnet7'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider8(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][8]
	name = 'vietnamnet8'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider9(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][9]
	name = 'vietnamnet9'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider10(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][10]
	name = 'vietnamnet10'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider11(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][11]
	name = 'vietnamnet11'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider12(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][12]
	name = 'vietnamnet12'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider13(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][13]
	name = 'vietnamnet13'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider14(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][14]
	name = 'vietnamnet14'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


class VietNamNetSpider15(VietNamNetSpider):
	category = newspaper_data['vietnamnet'][15]
	name = 'vietnamnet15'
	start_urls = ['https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(category)]


process = CrawlerProcess()
process.crawl(VietNamNetSpider)
process.crawl(VietNamNetSpider1)
process.crawl(VietNamNetSpider2)
process.crawl(VietNamNetSpider3)
process.crawl(VietNamNetSpider4)
process.crawl(VietNamNetSpider5)
process.crawl(VietNamNetSpider6)
process.crawl(VietNamNetSpider7)
process.crawl(VietNamNetSpider8)
process.crawl(VietNamNetSpider9)
process.crawl(VietNamNetSpider10)
process.crawl(VietNamNetSpider11)
process.crawl(VietNamNetSpider12)
process.crawl(VietNamNetSpider13)
process.crawl(VietNamNetSpider14)
process.crawl(VietNamNetSpider15)
process.start()