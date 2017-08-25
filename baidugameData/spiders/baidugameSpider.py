# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
import scrapy
import time
import re
from scrapy.conf import settings
import pymysql
from urllib import quote
from selenium import webdriver
from scrapy.selector import Selector
from baidugameData.items import BaidugamedataItem

class baidugameSpider(CrawlSpider):
    #用于区别Spider，同一个项目该名字必须是唯一的。
    name = "baidugameSpider"
    start_urls = ['https://baike.baidu.com/']

    base_baike = 'https://baike.baidu.com/item/'
    base_baidu = 'https://www.baidu.com/s?wd='
    base_tieba = 'http://tieba.baidu.com/f?kw='

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

    def get_game(self):
        sql = 'select game_name from gametestdata group by game_name'
        self.cursor.execute(sql)
        games = self.cursor.fetchall()
        dgame = []
        for game in games:
            if game not in dgame:
                dgame.append(game[0].strip())
        return dgame

    #获取搜索结果内容，并且获取下一页的链接
    def parse(self,response):
        games = self.get_game()
        for game in games:
            baidugamedataItem = BaidugamedataItem()
            engame =  quote(game.strip().encode('utf8'))
            #获取百度收录量
            baidu_link = self.base_baidu+engame
            baidu = scrapy.Request(baidu_link,callback=self.baidu_game_info)
            baidu.meta['baidugamedataItem'] = baidugamedataItem
            baidu.meta['engame'] = engame
            yield baidu

    #获取baidu搜索结果
    def baidu_game_info(self,response):
        print '[BAIDU]:',response.url
        baidugamedataItem = response.meta['baidugamedataItem']
        engame = response.meta['engame']
        baidugamedataItem['game_record'] = re.search(r'\D(\d+.*\d+)\D',''.join(response.xpath('//*[@id="container"]/div[2]/div/div[2]/text()').extract())).group(1)
        baidugamedataItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #获取贴吧帖子和会员数量
        tieba_link = self.base_tieba+engame+'&ie=utf-8'
        tieba = scrapy.Request(tieba_link,callback=self.tieba_game_info)
        tieba.meta['baidugamedataItem'] = baidugamedataItem
        tieba.meta['engame'] = engame
        yield tieba

    #获取tieba搜索结果
    def tieba_game_info(self,response):
        print '[TIEBA]:',response.url
        baidugamedataItem = response.meta['baidugamedataItem']
        engame = response.meta['engame']
        driver = webdriver.PhantomJS()
        driver.get(response.url)
        content = driver.page_source
        baidugamedataItem['game_fork'] = ''.join(Selector(text = content).xpath('//div[@id="pagelet_forum/pagelet/forum_card_number"]//span/span[2]/text()').extract())
        baidugamedataItem['game_post'] = ''.join(Selector(text = content).xpath('//div[@id="pagelet_forum/pagelet/forum_card_number"]/span/span[4]/text()').extract())
        driver.quit()
        #获取游戏信息
        baike_link = self.base_baike+engame+'?sefr=cr'
        baike = scrapy.Request(baike_link,callback=self.baike_game_info)
        baike.meta['baidugamedataItem'] = baidugamedataItem
        yield baike


    #获取baike搜索结果
    def baike_game_info(self,response):
        print '[BAIKE]:',response.url
        baidugamedataItem = response.meta['baidugamedataItem']
        baidugamedataItem['game_name'] = ''
        baidugamedataItem['game_type'] = ''
        baidugamedataItem['game_plat'] = ''
        baidugamedataItem['game_developer'] = ''
        baidugamedataItem['game_operator'] = ''
        baidugamedataItem['game_eng'] = ''
        baidugamedataItem['game_frame'] = ''
        baidugamedataItem['game_theme'] = ''
        baidugamedataItem['game_desc'] = ''.join(response.xpath('//div[3]/div[2]/div/div[2]/div[4]/div/text()').extract()).strip()
        baidugamedataItem['game_link'] = response.url
        baidugamedataItem['record_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for game_info in response.xpath('//div[@class="body-wrapper"]/div[2]/div/div[2]/div[@class="basic-info cmn-clearfix"]/dl'):
            i = 1
            for game in game_info.xpath('dt'):
                value_path = 'dd['+str(i)+']/text()'
                value_path_a = 'dd['+str(i)+']/a/text()'
                value_xpath = ''.join(game_info.xpath(value_path).extract()).strip()+''.join(game_info.xpath(value_path_a).extract()).strip()
                if ''.join(game.xpath('text()').extract()).strip() == u'中文名':
                    baidugamedataItem['game_name'] = value_xpath
                if ''.join(game.xpath('text()').extract()).strip() == u'游戏类型':
                    baidugamedataItem['game_type'] = value_xpath
                if ''.join(game.xpath('text()').extract()).strip() == u'游戏平台':
                    baidugamedataItem['game_plat'] = value_xpath
                if ''.join(game.xpath('text()').extract()).strip() == u'开发商':
                    baidugamedataItem['game_developer'] = value_xpath
                if ''.join(game.xpath('text()').extract()).strip() == u'发行商':
                    baidugamedataItem['game_operator'] = value_xpath
                if ''.join(game.xpath('text()').extract()).strip() == u'游戏引擎':
                    baidugamedataItem['game_eng'] = value_xpath
                if ''.join(game.xpath('text()').extract()).strip() == u'游戏画面':
                    baidugamedataItem['game_frame'] = value_xpath
                if ''.join(game.xpath('text()').extract()).strip() == u'内容主题':
                    baidugamedataItem['game_theme'] = value_xpath
                i+=1
        yield baidugamedataItem