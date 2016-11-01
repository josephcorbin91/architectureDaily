
    # -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArchitecturedailyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    id = scrapy.Field()
    title = scrapy.Field()
    city = scrapy.Field()
    description = scrapy.Field()
    video = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()	
    date = scrapy.Field()
    like = scrapy.Field()
    
class ThreadItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    
    link = scrapy.Field()
    threadDescription = scrapy.Field()
    
