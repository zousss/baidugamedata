# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings
from baidugameData.items import BaidugamedataItem

class BaidugamedataPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            use_unicode= True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        if item.__class__ == BaidugamedataItem:
            try:
                sql = 'INSERT INTO baidugameData VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                param = (item['game_link'],item['game_name'],item['game_type'],item['game_frame'],item['game_plat'], \
                         item['game_theme'],item['game_developer'], \
                         item['game_operator'],item['game_eng'], \
                         item['game_desc'],item['game_fork'],item['game_post'],item['game_record'], \
                         item['record_time'])
                self.cursor.execute(sql,param)
                self.connect.commit()
            except pymysql.Warning,w:
                print "Warning:%s" % str(w)
            except pymysql.Error, e:
                print "Error:%s" % str(e)
        return item
