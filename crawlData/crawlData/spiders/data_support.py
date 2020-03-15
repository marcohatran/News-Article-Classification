import os 
import datetime 

# Lists of categories of newspaper (categories that have the same HTML structure)
thanhnien_categories = ['thoi-su', 'the-gioi', 'tai-chinh-kinh-doanh', 'doi-song', 'van-hoa', 'gioi-tre', 'giao-duc', 'suc-khoe', 'du-lich', 'cong-nghe']
    # goc-nhin, so-hoa
    # done: ['thoi-su']
vnexpress_categories = ['the-gioi', 'phap-luat' ,'giao-duc' , 'khoa-hoc','oto-xe-may' , 'y-kien' ,'tam-su',  'cuoi', 'kinh-doanh', 'giai-tri', 'the-thao', 'suc-khoe', 'doi-song', 'du-lich']
    # cong-nghe, du-lich, the-thao
tuoitre_categories = ['thoi-su', 'the-gioi', 'phap-luat', 'kinh-doanh', 'xe', 'nhip-song-tre', 'van-hoa', 'giai-tri', 'giao-duc', 'khoa-hoc', 'suc-khoe', 'gia-that', 'ban-doc-lam-bao']
    # du-lich
dantri_categories = ['su-kien', 'xa-hoi', 'the-gioi', 'the-thao', 'giao-duc-khuyen-hoc', 'tam-long-nhan-ai', 'kinh-doanh', 'bat-dong-san', 'van-hoa', 'giai-tri', 'phap-luat', 'nhip-song-tre', 'suc-khoe', 'suc-manh-so', 'o-to-xe-may', 'tinh-yeu-gioi-tinh']
vietnamnet_categories = ['thoi-su/chinh-tri/', 'talkshow', 'thoi-su', 'kinh-doanh', 'giai-tri', 'the-gioi', 'giao-duc', 'doi-song', 'phap-luat', 'the-thao', 'cong-nghe', 'suc-khoe', 'bat-dong-san', 'ban-doc', 'tuanvietnam', 'oto-xe-may']
laodong_categories = ['thoi-su', 'cong-doan', 'the-gioi', 'xa-hoi', 'phap-luat', 'kinh-te', 'bat-dong-san', 'van-hoa-giai-tri', 'the-thao', 'xe', 'suc-khoe', 'ban-doc', 'tam-long-vang']
nhandan_categories = ['chinhtri', 'kinhte', 'vanhoa', 'xahoi', 'phapluat', 'du-lich', 'thegioi', 'thethao', 'giaoduc', 'y-te', 'khoahoc-congnghe', 'bandoc']
doisongvaphapluat_categories = ['phap-luat', 'kinh-doanh', 'doi-song', 'giao-duc', 'giai-tri', 'the-thao', 'cong-nghe']
vov_categories = ['chinh-tri', 'doi-song', 'the-gioi', 'kinh-te', 'xa-hoi', 'phap-luat', 'the-thao', 'van-hoa-giai-tri', 'quan-su-quoc-phong', 'suc-khoe', 'oto-xe-may']

# Dict store name and categories of newspaper 
newspaper_data = {'thanhnien' :         thanhnien_categories        , 
                  'vnexpress' :         vnexpress_categories        , 
                  'tuoitre'   :         tuoitre_categories          , 
                  'dantri'    :         dantri_categories           , 
                  'vietnamnet':         vietnamnet_categories       ,
                  'laodong'   :         laodong_categories          , 
                  'nhandan'   :         nhandan_categories          , 
                  'doisongvaphapluat':  doisongvaphapluat_categories, 
                  'vov':                vov_categories              ,
                  }


# data file structure
    # day_crawl - datetime
        # name - name of newspaper
            # category 

    # stats - contains statistical data
        # stats + datetime.txt

# Get the date time for creating folders
dt = datetime.datetime.today()
dt = str(dt.day) + "-" + str(dt.month) + "-" + str(dt.year)

# Create struture before crawling data
def createDataStructure():
    # create day_crawl folder
    day_crawl = "data" + "\\" + dt
    if not os.path.exists(day_crawl):
        os.mkdir(day_crawl)

    # create categories folder 
    for newspaper in newspaper_data:
        # Create folder whose name is name of the newspaper
        name_folder = day_crawl + "\\" + newspaper
        if not os.path.exists(name_folder):
            os.mkdir(name_folder)
        
def write_log(name, category, string):
    # name: name of the newspaper
    # category: classes
    string = str(string)
    noInfo = ['–', '-', '*', '...', '>>', '(Dân trí)', 'Xem tiếp']
    for i in noInfo:
        string = string.replace(i, '')
    # remove spaces at first
    string = string.strip()
    
    # substitue many spaces to only one
    # string = ' '.join(string.split())

    if string == '':
        pass
    else:
        # construct filename of the text
        text_file = "data" + "\\" + dt + "\\" + name + "\\" + category + ".txt"
        # mode a means inserted data at the end of the file 
        # create the file if it is not exist 
        # save to txt file
        log = open(text_file, "a", encoding="utf-8")
        log.write('\n\n\n' + string)
        # any risk when close and open too much ?
        log.close()

# Write log about statistical information about data each time crawl (locally)
def getStatsLocal():
    return 

# Write log about statistical information about all data (globally)
def getStatsGlobal():
    return


createDataStructure()