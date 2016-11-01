# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class ArchitecturedailyItemPipeline(object):
    def process_item(self, item, spider):
        if item['like'] and not item['like'].isspace() and item['image'] and not item['image'].isspace():
            return item
        else:
            return DropItem("Not Enough Likes")
            
            
            
class ArchitecturedailyThreadPipeline(object):
    def process_item(self, item, spider):
        if item['link'] and not item['link'].isspace():
            return item
        else:
            return DropItem("No Links")


        
