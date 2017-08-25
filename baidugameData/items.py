# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidugamedataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_link = scrapy.Field()
    game_name = scrapy.Field()
    game_plat = scrapy.Field()
    game_frame = scrapy.Field()
    game_developer = scrapy.Field()
    game_operator = scrapy.Field()
    game_theme = scrapy.Field()
    game_type = scrapy.Field()
    game_desc = scrapy.Field()
    game_eng = scrapy.Field()
    game_fork = scrapy.Field()
    game_post = scrapy.Field()
    game_record = scrapy.Field()
    record_time = scrapy.Field()
