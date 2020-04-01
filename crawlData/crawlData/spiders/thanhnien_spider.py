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

crawl_newspaper = 'thanhnien'

# Thanh nien Online
class ThanhNienSpider(scrapy.Spider):
    name = 'thanhnien'
    category = newspaper_data['thanhnien'][0]
    start_urls = ['https://thanhnien.vn/' + category]
    crawled_big_titles = False
    page_count = 0
    def getCategory(self, url):
        category = str(url).replace('https://thanhnien.vn/', '').replace('/', '')
        category = re.sub('p\d+', '', category)
        return category.replace('-', '')
    
    def getTitle(self, response):
        new_title = ''.join(response.css('a.story__title::text').getall())
        return new_title

    def getDescription(self, response):
        description = ''.join(response.css('div.summary ::text').getall())
        return description.rstrip()

    def getContentAndSaveData(self, response, category, title, description = ''):
        body = response.css("div.l-content")
        raw_content = body.css("div#abody.cms-body.detail ::text").getall()
        # no infomation text
        trash = body.css("div#abody.cms-body.detail").css(".video ::text").getall()
        trash += body.css("div#abody.cms-body.detail").css("script ::text").getall()
        trash += body.css("div#abody.cms-body.detail").css("table ::text").getall()
        clean_text = []
        for text in raw_content:
            if text in trash:
                pass
            else:
                clean_text.append(text)

        content = ''.join(clean_text).replace('\r', '')
        content = re.sub('\n+', '\n', content).strip()
        write_log(crawl_newspaper, self.category, title + '\n' + description + content)

    def parse(self, response):
        category = self.getCategory(response.url)
        # Crawl from the big titles first - just run one time
        feature = response.css('div.feature')
        if not self.crawled_big_titles:
            for new in feature.css('article'):
                title = self.getTitle(new)
                link_content = new.css("a::attr(href)").get()
                if link_content is not None:
                    yield scrapy.Request(
                        response.urljoin(link_content),
                        callback=self.getContentAndSaveData,
                        cb_kwargs={'category': category,
                                   'title': title}
                    )
        self.crawled_big_titles = True
            
        # contains small titles and summary
        relative = response.css('div.relative')
        # print(len(relative))

        # small news title and summary
        for new in relative.css('article.story'):
            title = self.getTitle(new)
            description = self.getDescription(new)
            link_content = new.css("a::attr(href)").get()
            if link_content is not None:
                
                yield scrapy.Request(
                    response.urljoin(link_content),
                    callback=self.getContentAndSaveData,
                    cb_kwargs={'category': category,
                                'title': title,
                                'description': description}
                )

        # go to next page
        next_page = response.css('div.zone--timeline').css('ul').css('li ::attr(href)').getall()
        # print(next_page)
        if next_page is not None:
            if self.page_count == 0:
                next_page = next_page[0]
                self.page_count += 1
            elif self.page_count == 1:
                next_page = next_page[1]
                self.page_count += 1
            else:
                next_page = next_page[2]
            # print(next_page)

            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
print(len(newspaper_data[crawl_newspaper]))


class ThanhNienSpider1(ThanhNienSpider):
    category = newspaper_data['thanhnien'][1]
    name = 'thanhnien1' 
    start_urls = ['https://thanhnien.vn/' + category]

class ThanhNienSpider2(ThanhNienSpider):
    category = newspaper_data['thanhnien'][2]
    name = 'thanhnien2' 
    start_urls = ['https://thanhnien.vn/' + category]

class ThanhNienSpider3(ThanhNienSpider):
    category = newspaper_data['thanhnien'][3]
    name = 'thanhnien3' 
    start_urls = ['https://thanhnien.vn/' + category]

class ThanhNienSpider4(ThanhNienSpider):
    category = newspaper_data['thanhnien'][4]
    name = 'thanhnien4' 
    start_urls = ['https://thanhnien.vn/' + category]

class ThanhNienSpider5(ThanhNienSpider):
    category = newspaper_data['thanhnien'][5]
    name = 'thanhnien5' 
    start_urls = ['https://thanhnien.vn/' + category]

class ThanhNienSpider6(ThanhNienSpider):
    category = newspaper_data['thanhnien'][6]
    name = 'thanhnien6' 
    start_urls = ['https://thanhnien.vn/' + category]

class ThanhNienSpider7(ThanhNienSpider):
    category = newspaper_data['thanhnien'][7]
    name = 'thanhnien7' 
    start_urls = ['https://thanhnien.vn/' + category]

class ThanhNienSpider8(ThanhNienSpider):
    category = newspaper_data['thanhnien'][8]
    name = 'thanhnien8' 
    start_urls = ['https://thanhnien.vn/' + category]

class ThanhNienSpider9(ThanhNienSpider):
    category = newspaper_data['thanhnien'][9]
    name = 'thanhnien9' 
    start_urls = ['https://thanhnien.vn/' + category]


process = CrawlerProcess()
process.crawl(ThanhNienSpider2)
process.crawl(ThanhNienSpider3)
process.crawl(ThanhNienSpider4)
process.crawl(ThanhNienSpider5)
process.crawl(ThanhNienSpider6)
process.crawl(ThanhNienSpider7)
process.crawl(ThanhNienSpider8)
process.crawl(ThanhNienSpider9)