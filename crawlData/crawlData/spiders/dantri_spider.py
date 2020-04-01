import scrapy 
import os
import re
try:    
    from crawl_new_support import write_log, newspaper_data, createSpider
except:
    pass
try:
    from crawlData.spiders.crawl_new_support import write_log, newspaper_data, createSpider
except:
    pass
from scrapy.crawler import CrawlerProcess
print(os.getcwd())
crawl_newspaper = 'dantri'

# Dan Tri
class DanTriSpider(scrapy.Spider):  
    name = "dantri"
    category = newspaper_data[crawl_newspaper][0]
    # start_urls = ['https://dantri.com.vn/' + sub_page + '.htm' for sub_page in newspaper_data[name]]
    start_urls = ['https://dantri.com.vn/' + category + '.htm']
   
    def getTitle(self, response):
        title = response.css('div.mr1').css('h2').css('a ::text').getall()
        title = ''.join(title)
        return title

    def getDescription(self, response):
        raw_description = response.css('div.fon5.wid324.fl ::text').getall()
        trash = response.css('div.fon5.wid324.fl').css("h3.h3relate ::text").getall()
        description = []
        for des in raw_description:
            if des in trash:
                pass
            else:
                description.append(des)
        description = ''.join(description)
        description = ''.join(description).replace('\r', '')
        description = re.sub('\n+', '\n', description).strip()
        return description

    def getContentAndSaveData(self, response, title, description=''):
        content = ''.join(response.css("#divNewsContent").css("p ::text").getall())
        content = ''.join(content).replace('\r', '')
        content = re.sub('\n+', '\n', content).strip()
        write_log(crawl_newspaper, self.category, title + '\n' + description + content)
    
    def parse(self, response):
        new_list = response.css('div.clearfix')
        # category = str(response.url).replace('https://dantri.com.vn/', '').replace('/', '').replace('.htm', '')
        for new in new_list.css('div.mt3.clearfix.eplcheck'):
            
            title = self.getTitle(new)
            # write_log(self.name, category, title)

            description = self.getDescription(new)

            link_content = new.css(" ::attr(href)").get()
            if link_content is not None:
                yield scrapy.Request(
                    response.urljoin(link_content),
                    callback=self.getContentAndSaveData,
                    cb_kwargs={
                    'title': title,
                    'description': description
                    }
                )
        next_page = response.css('div.clearfix.mt1').css('div.fr ::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
                )
            


# # print(len(newspaper_data[crawl_newspaper]))
# createSpider(class_name='DanTri', newspaper_name=crawl_newspaper, 
#              nums_of_spiders = len(newspaper_data[crawl_newspaper]), 
#              url = 'https://dantri.com.vn/', extra_url='.htm')

class DanTriSpider1(DanTriSpider):
    category = newspaper_data['dantri'][1]
    name = 'dantri1'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider2(DanTriSpider):
    category = newspaper_data['dantri'][2]
    name = 'dantri2'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider3(DanTriSpider):
    category = newspaper_data['dantri'][3]
    name = 'dantri3'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider4(DanTriSpider):
    category = newspaper_data['dantri'][4]
    name = 'dantri4'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider5(DanTriSpider):
    category = newspaper_data['dantri'][5]
    name = 'dantri5'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider6(DanTriSpider):
    category = newspaper_data['dantri'][6]
    name = 'dantri6'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider7(DanTriSpider):
    category = newspaper_data['dantri'][7]
    name = 'dantri7'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider8(DanTriSpider):
    category = newspaper_data['dantri'][8]
    name = 'dantri8'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider9(DanTriSpider):
    category = newspaper_data['dantri'][9]
    name = 'dantri9'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider10(DanTriSpider):
    category = newspaper_data['dantri'][10]
    name = 'dantri10'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider11(DanTriSpider):
    category = newspaper_data['dantri'][11]
    name = 'dantri11'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider12(DanTriSpider):
    category = newspaper_data['dantri'][12]
    name = 'dantri12'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider13(DanTriSpider):
    category = newspaper_data['dantri'][13]
    name = 'dantri13'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider14(DanTriSpider):
    category = newspaper_data['dantri'][14]
    name = 'dantri14'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


class DanTriSpider15(DanTriSpider):
    category = newspaper_data['dantri'][15]
    name = 'dantri15'
    start_urls = ['https://dantri.com.vn/' + category + '.htm']


process = CrawlerProcess()
process.crawl(DanTriSpider)
process.crawl(DanTriSpider1)
process.crawl(DanTriSpider2)
process.crawl(DanTriSpider3)
process.crawl(DanTriSpider4)
process.crawl(DanTriSpider5)
process.crawl(DanTriSpider6)
process.crawl(DanTriSpider7)
process.crawl(DanTriSpider8)
process.crawl(DanTriSpider9)
process.crawl(DanTriSpider10)
process.crawl(DanTriSpider11)
process.crawl(DanTriSpider12)
process.crawl(DanTriSpider13)
process.crawl(DanTriSpider14)
process.crawl(DanTriSpider15)
process.start()

