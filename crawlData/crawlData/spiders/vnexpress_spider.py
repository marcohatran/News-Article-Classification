import scrapy 
import os
import re
from crawlData.spiders.data_support import write_log, newspaper_data

crawl_newspaper = 'vnexpress'

# VnExpress
class VnExpressSpider(scrapy.Spider):
    name = "vnexpress"
    start_urls = ['https://vnexpress.net/' + sub_page for sub_page in newspaper_data[name]]
    # return the category of the article crawled
    def getCategory(self, url):
        # remove domain name
        category = str(url).replace('https://vnexpress.net/', '').replace('/', '')
        category = re.sub('p\d+', '', category)
        return category.replace('-', '')

    def getTitle(self, response, category):
        new_title = ''.join(response.css('h4.title_news ::text').getall())
        # write_log(self.name, category, new_title)
        return new_title

    def getDescription(self, response, category):
        location_stamp = response.css('span.location-stamp ::text').getall()
        location_stamp = ''.join(location_stamp)
            
        new_description = ''.join(response.css('p.description').css('a ::text').getall())
        new_description = new_description.replace(location_stamp, '')
        # write_log(self.name, category, new_description)
        return new_description

    def getContentAndSaveData(self, response, category, title, description):
        article = response.css('section.sidebar_1').css('article.content_detail.fck_detail.width_common.block_ads_connect')
        content = ''
        # may improve by concat the list
        for cont in article.css('p'):
            cont = cont.css(".Normal ::text").getall()
            content += ''.join(cont).replace('\n', '') +'\n'
        author_name = article.css('p').css('strong ::text').getall()
        author_name = ''.join(author_name)
        content = content.replace(author_name, '')
        content = re.sub('\n+', '\n', content).strip() 
            # write_log(self.name, category, content)
        # write all data
        write_log(crawl_newspaper, category, title.rstrip() + '\n' + description.rstrip() + content)

    def parse(self, response):
        # find category of newspaper
        category = self.getCategory(response.url)

        sidebar_1 = response.css('section.sidebar_1')
        for new in sidebar_1.css('article.list_news'):
            # logging the title
            title = self.getTitle(new, category)

            # logging the description
            description = self.getDescription(new, category)

            # logging the content 
            link_content = new.css('a::attr(href)').get()
            if link_content is not None:
                yield scrapy.Request(response.urljoin(link_content), 
                                    callback=self.getContentAndSaveData,
                                    # dict of additional arguments for callback function
                                    cb_kwargs={'category': category, 'title': title, 'description': description},
                                    dont_filter=True)

        # continue crawling on next page
        next_page = response.css('.pagination.mb10').css('a.next::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(
            response.urljoin(next_page),
            callback=self.parse)

class VnExpressSpider2(VnExpressSpider):
    category = newspaper_data['vnexpress'][2]
    name = 'vnexpress2' 
    start_urls = ['https://vnexpress.net/' + category]

class VnExpressSpider3(VnExpressSpider):
    category = newspaper_data['vnexpress'][3]
    name = 'vnexpress3'
    start_urls = ['https://vnexpress.net/' + category]

class VnExpressSpider4(VnExpressSpider):
    category = newspaper_data['vnexpress'][4]
    name = 'vnexpress4'
    start_urls = ['https://vnexpress.net/' + category]

class VnExpressSpider5(VnExpressSpider):
    category = newspaper_data['vnexpress'][5]
    name = 'vnexpress5'
    start_urls = ['https://vnexpress.net/' + category]

class VnExpressSpider6(VnExpressSpider):
    category = newspaper_data['vnexpress'][6]
    name = 'vnexpress6'
    start_urls = ['https://vnexpress.net/' + category]

class VnExpressSpider7(VnExpressSpider):
    category = newspaper_data['vnexpress'][7]
    name = 'vnexpress7'
    start_urls = ['https://vnexpress.net/' + category]

class VnExpressSpider8(VnExpressSpider):
    category = newspaper_data['vnexpress'][8]
    name = 'vnexpress8'
    start_urls = ['https://vnexpress.net/' + category]

class VnExpressSpider9(VnExpressSpider):
    category = newspaper_data['vnexpress'][9]
    name = 'vnexpress9'
    start_urls = ['https://vnexpress.net/' + category]
    # duplicated 7 and 9 -> remove duplicated later
# then run again 7 or 9
class VnExpressSpider10(VnExpressSpider):
    category = newspaper_data['vnexpress'][10]
    name = 'vnexpress10'
    start_urls = ['https://vnexpress.net/' + category]

class VnExpressSpider11(VnExpressSpider):
    category = newspaper_data['vnexpress'][11]
    name = 'vnexpress11'
    start_urls = ['https://vnexpress.net/' + category]

class VnExpressSpider12(VnExpressSpider):
    category = newspaper_data['vnexpress'][12]
    name = 'vnexpress12'
    start_urls = ['https://vnexpress.net/' + category]
# end here
class VnExpressSpider13(VnExpressSpider):
    category = newspaper_data['vnexpress'][13]
    name = 'vnexpress13'
    start_urls = ['https://vnexpress.net/' + category]

# clean some duplicated news
# maybe manualy remove author name in the paper for more cleaning
# 