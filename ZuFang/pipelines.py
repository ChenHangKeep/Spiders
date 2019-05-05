# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import pymysql
import pymongo

#使用sqlite
class ZufangPipeline(object):
    def open_spider(self, spider):
        self.con = sqlite3.connect('zufang.sqlite')
        self.cu = self.con.cursor()

    def process_item(self, item, spider):
        print(spider.name, 'pipelines')
        insert_sql = "insert into zufang (title, money) values('{}','{}')".format(item['title'],item['money'])
        print(insert_sql)
        self.cu.execute(insert_sql)
        self.con.commit()
        return item

    def close_spider(self, spider):
        self.con.close()


#使用MySQL
class ZuFangDetailPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='ganji_detail',  # 数据库名
            user='root',  # 数据库用户名
            passwd='root',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    # def open_spider(self, spider):
    #     self.con = sqlite3.connect('zufang_detail.sqlite')
    #     self.cu = self.con.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into ganji_detail(title, money, payment, house_type, area, direction, floor, fitment_type, address)
            value (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (item['title'],
             item['money'],
             item['payment'],
             item['house_type'],
             item['area'],
             item['direction'],
             item['floor'],
             item['fitment_type'],
             item['address'],))
        self.connect.commit()
        return item  # 必须实现返回


#使用MongoDB
class ZuFangDetailPipelineMongoDB(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        scrapy_db = client['ganji']
        self.col1 = scrapy_db['ganji_detail']

    def process_item(self, item, spider):
        self.col1.insert_one(item)
        return item
#     # collection = 'military_affairs'
#
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         '''
#             scrapy为我们访问settings提供了这样的一个方法，这里，
#             我们需要从settings.py文件中，取得数据库的URI和数据库名称
#         '''
#
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DB')
#         )
#
#
#     def open_spider(self, spider):
#         '''
#         爬虫一旦开启，就会实现这个方法，连接到数据库
#         '''
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#
#     def close_spider(self, spider):
#         '''
#         爬虫一旦关闭，就会实现这个方法，关闭数据库连接
#         '''
#         self.client.close()
#
#
#     def process_item(self, item, spider):
#         '''
#             每个实现保存的类里面必须都要有这个方法，且名字固定，用来具体实现怎么保存
#         '''
#         if not item['title']:
#             return item
#
#         data = {
#             'title': item['title'][0],
#             'content': item['content']
#         }
#         table = self.db[self.collection]
#         table.insert_one(data)
#         return item



# title, money, payment, house_type, area, direction, floor, fitment_type, address
