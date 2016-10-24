import scrapy, json

from architectureDaily.items import ThreadItem



class ArchitectureSpider(scrapy.Spider):
    
    city="London"
    name = "get_threads"
    allowed_domains = ["skyscrapercity.com"]
    start_urls = ["http://www.skyscrapercity.com/forumdisplay.php?f=905"]

    def parse(self, response):
        for sel in response.xpath('//td[contains(@id, "threadtitle")]'):
            delimiter = "|"        
            item = ThreadItem()        
            threadDesc = ''.join(sel.xpath('normalize-space(.//a[contains(@id,"thread_title")]/text())').extract())
            print(threadDesc)
            pos = threadDesc.find(delimiter)
            print(pos)
            print(threadDesc[pos])
            item['threadDescription'] = threadDesc[0:pos].strip()
            item['link'] = ''.join(sel.xpath('normalize-space(.//a[contains(text(),"Last Page")]/@href)').extract())
            yield item
       