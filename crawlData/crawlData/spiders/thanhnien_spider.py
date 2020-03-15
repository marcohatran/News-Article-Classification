import scrapy 
import os
import re
from crawlData.spiders.data_support import write_log, newspaper_data
from scrapy.crawler import CrawlerProcess

crawl_newspaper = 'thanhnien'

# Thanh nien Online
class ThanhNienSpider(scrapy.Spider):
    name = 'thanhnien'
    start_urls = ['https://thanhnien.vn/' + sub_page + '/' for sub_page in newspaper_data[name]]
    crawled_big_titles = False
    def getCategory(self, url):
        category = str(url).replace('https://thanhnien.vn/', '').replace('/', '')
        category = re.sub('p\d+', '', category)
        return category.replace('-', '')
    
    def getTitle(self, response):
        new_title = ''.join(response.css('a.story__title::text').getall())
        return new_title

    def getDescription(self, response):
        description = ''.join(response.css('div.summary ::text').getall())
        return description

    def getContentAndSaveData(self, response, category, title, description = ''):
        content = ''
        write_log(crawl_newspaper, category, title + description + content)

    def parse(self, response):
        category = self.getCategory(response.url)
        # Crawl from the big titles first - just run one time
        feature = response.css('div.feature')
        if not self.crawled_big_titles:
            for new in feature.css('article'):
                title = self.getTitle(new)
                link_content = new.css("a::atrr(href)").get()
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

        # small news title and summary
        for new in relative.css('article.story'):
            title = self.getTitle(new)
            description = self.getDescription(new)
            link_content = new.css("a::atrr(href)")
            if link_content is not None:
                yield scrapy.Request(
                    response.urljoin(link_content),
                    callback=self.getContentAndSaveData,
                    cb_kwargs={'category': category,
                                'title': title,
                                'description': description}
                )

        # go to next page
        next_page = response.css('ul.pagination').css('li::atrr(href)').get()
        if next_page is not None:
            print(next_page)
            yield scrapy.Request(
                response.urljoin(link_content),
                callback=self.parse
            )
print(len(newspaper_data[crawl_newspaper]))

# process = CrawlerProcess()
# process.crawl(ThanhNienSpider)
# process.start()