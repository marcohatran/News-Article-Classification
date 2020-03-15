import scrapy 
import os
import re
from crawlData.spiders.data_support import write_log, newspaper_data

# VnExpress
class VnExpressSpider(scrapy.Spider):
    name = "vnexpressxxxx"
    start_urls = ['https://vnexpress.net/' + sub_page for sub_page in newspaper_data[name]]

    def getContent(self, response, category):
        print('Hi')
        article = response.css('section.sidebar_1').css('article.content_detail.fck_detail.width_common.block_ads_connect')
        for content in article.css('p.Normal ::text').getall():
            content = ''.join(content)
            write_log(self.name, category, content)

    def getTextData(self, response, category):
        content_links = []
        sidebar_1 = response.css('section.sidebar_1')
        for new in sidebar_1.css('article.list_news'):
            # get the title of the news
            new_title = ''.join(new.css('h4.title_news ::text').getall())
            write_log(self.name, category, new_title)

            # get the link contains content of news
            link = new.css('a::attr(href)').get()
       
            if link:
                content_links.append(link)
            # take the description 
            location_stamp = new.css('span.location-stamp ::text').getall()
            location_stamp = ''.join(location_stamp)
            
            new_description = ''.join(new.css('p.description').css('a ::text').getall())
            new_description = new_description.replace(location_stamp, '')
            write_log(self.name, category, new_description)
        return content_links

    def parse(self, response):
        category = str(response.url).replace('https://vnexpress.net/', '').replace('/', '')
        category = re.sub('p\d+', '', category)
        category = re.sub('-pd+', '', category)
        # print(category)
        content_links = self.getTextData(response, category)
        # get the content inside
        for link in content_links:
            yield scrapy.Request(response.urljoin(link), callback=self.getContent, cb_kwargs={'category': category})
        # find the new links 
        next_page = response.css('.pagination.mb10').css('a.next::attr(href)').get()
        # print(next_page)
        if next_page:
            yield scrapy.Request(
            response.urljoin(next_page),
            callback=self.parse)


# Thanh nien Online
class ThanhNienSpider(scrapy.Spider):
    name = 'thanhnien'
    start_urls = ['https://thanhnien.vn/' + sub_page + '/' for sub_page in newspaper_data[name]]

    def parse(self, response):
        # contains big titles
        feature = response.css('div.feature')
        # contains small titles and summary
        relative = response.css('div.relative')
    
        category = str(response.url).replace('https://thanhnien.vn/', '').replace('/', '')
        # first new
        # big titles 
        for title in feature.css('article'):
            string_title = ''.join(title.css('a.story__title::text').getall())
            write_log(self.name, category, string_title)
        # small news title and summary
        for new in relative.css('article.story'):
            string_title = ''.join(new.css('a.story__title::text').getall())
            write_log(self.name, category, string_title)
            summary_title = ''.join(new.css('div.summary ::text').getall())
            write_log(self.name, category, summary_title)
            

        

# Tuoi Tre Online
class TuoiTreSpider(scrapy.Spider):
    name = "tuoitre"
    start_urls = ['https://tuoitre.vn/' + sub_page + '.htm' for sub_page in newspaper_data[name]]
    def parse(self, response):
        category = str(response.url).replace('https://tuoitre.vn/', '').replace('/', '').replace('.htm', '')
        content = response.css('div.content.w980.list.' + category)
        big_titles = content.css('ul.focus-bottom-ul')
        for title in big_titles.css('a.focus-middle-title ::text'):
            string = ''.join(title.getall())
            write_log(self.name, category, string)

        small_titles = content.css('ul.list-news-content')
        for title in small_titles.css('li.news-item'):
            string = title.css('h3.title-news').css('a ::text').getall()
            string = ''.join(string)
            write_log(self.name, category, string)

            summary = ''.join(title.css('p.sapo ::text').getall())
            if summary[0:3] == 'TTO':
                summary = summary[3:]
            write_log(self.name, category, summary)

            extra_title = ''.join(title.css('div.news-extra-one.no-thumb ::text').getall())
            write_log(self.name, category, extra_title)
    


# Dan Tri
class DanTriSpider(scrapy.Spider):
    name = "dantri"
    start_urls = ['https://dantri.com.vn/' + sub_page + '.htm' for sub_page in newspaper_data[name]]
    def parse(self, response):
        clear_fix = response.css('div.clearfix')
        category = str(response.url).replace('https://dantri.com.vn/', '').replace('/', '').replace('.htm', '')
        for timeline in clear_fix.css('div.mt3.clearfix.eplcheck'):
            
            string = timeline.css('div.mr1').css('h2').css('a ::text').getall()
            string = ''.join(string)
            write_log(self.name, category, string)

            summary = timeline.css('div.fon5.wid324.fl ::text').getall()
            
            for sth in summary:
                write_log(self.name, category, sth)



# VietNamNet
class VietNamNetSpider(scrapy.Spider):
    name = "vietnamnet"
    start_urls = ['https://vietnamnet.vn/vn/' + sub_page + '/trang%d/' %i for sub_page in newspaper_data[name] for i in range(1, 5)]
    def parse(self, response):
        category = str(response.url).replace('https://vietnamnet.vn/vn/', '').replace('/', '').replace('.htm', '')
        category = re.sub('trang\d', '', category)
        list_news = response.css('div.list-content.list-content-loadmore.lagre.m-t-20.clearfix')
        for new in list_news.css('div.clearfix.item'):
            title = new.css('div.d-ib.w-400').css('h3 ::text').getall()
            title = ''.join(title)
            write_log(self.name, category, title)

            summary = new.css('div.lead ::text').getall()
            summary = ''.join(summary)
            write_log(self.name, category, summary)

# Lao Dong
class LaoDongSpider(scrapy.Spider):
    name = "laodong"
    start_urls = ['https://laodong.vn/' + sub_page + '/'  for sub_page in newspaper_data[name]]

    def parse(self, response):
        category = str(response.url).replace('https://laodong.vn/', '').replace('/', '').replace('.htm', '')
        big_news = response.css('.ul.list-feature.feature-v-1.m-y-0')
        for new in big_news.css('li'):
            title = new.css('header ::text').getall()
            title = ''.join(title)
            write_log(self.name, category, title)

        small_news = response.css('ul.list-main-content.list-main-new')
        for new in small_news.css('li'):
            title = new.css('header ::text').getall()
            title = ''.join(title)
            write_log(self.name, category, title)

            summary = new.css('p::text').getall()
            summary = ''.join(summary)
            write_log(self.name, category, summary)

# Nhan Dan
class NhanDanSpider(scrapy.Spider):
    name = "nhandan"
    start_urls = ['https://nhandan.com.vn/' + sub_page for sub_page in newspaper_data[name]]

    def cleanText(self, string):    
        noInfo = ['NDĐT', '–', '-', '[Infographic]', '*']
        for i in noInfo:
            string = string.replace(i, '')
        string = string.strip()
        return string

    def parse(self, response):
        category = str(response.url).replace('https://nhandan.com.vn/', '').replace('/', '').replace('.htm', '')
        # print(category, response.url)
        hot_news = response.css('div.hotnew-container.lop3')
        for new in hot_news.css('div.media.content-box'):
            
            title = new.css('h5.mt-0 ::text').getall()
            title = ''.join(title)
            write_log(self.name, category, self.cleanText(title))
            # print(title)

            body = new.css('div.media-body').css('p ::text').getall()
            body = ''.join(body)
            write_log(self.name, category, self.cleanText(body))

# Doi song va Phap Luat
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
        
# VOV
class vovSpider(scrapy.Spider):
    name = 'vov'
    start_urls = ['https://vov.vn/' + sub_page + '/' for sub_page in newspaper_data[name]]
    
    def cleanText(self, string):    
        noInfo = ['VOV.VN']
        for i in noInfo:
            string = string.replace(i, '')
        string = string.strip()
        return string
    
    def parse(self, response):
        category = str(response.url).replace('https://vov.vn/', '').replace('/', '').replace('.htm', '')
        selectors = ['div.stories-style-9', 'div.wrap', 'div.stories-style-6']

        for selector in selectors:
            stories = response.css(selector)
            for story in stories.css('article.story'):
                title = story.css('div.story__heading ::text').getall()
                title = ''.join(title)
                write_log(self.name, category, self.cleanText(title))

                desc = story.css('p.story__desc ::text').getall()
                desc = ''.join(desc)
                write_log(self.name, category, self.cleanText(desc))
       
