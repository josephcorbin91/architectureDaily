import scrapy, json

from architectureDaily.items import ArchitecturedailyItem



class ArchitectureSpider(scrapy.Spider):
	
          

    
    city="London"
    name = "get_posts"
    allowed_domains = ["skyscrapercity.com"]
    start_urls = [
		"http://www.skyscrapercity.com/showthread.php?t=315079&page=941"
    ]

    def parse(self, response):
        for sel in response.xpath('//td[contains(@id, "td_post")]'): 
            item = ArchitecturedailyItem()        
            item['id'] = ''.join(sel.xpath('normalize-space(@id)').extract())
            #item['title'] = sel.xpath('normalize-space(div[contains(@id, "post_message")]/text() | div[contains(@id, "post_message")]//*/text())').extract()
            item['title'] = ''.join(sel.xpath('normalize-space(div[contains(@id, "post_message")]/text())').extract())
            item['image'] = sel.xpath('normalize-space(div[contains(@id, "post_message")]/img/@src)').extract_first(default='https://d13yacurqjgara.cloudfront.net/users/370014/screenshots/1738726/teste-4-drble_1x.jpg')
            item['like'] = ''.join(sel.xpath('normalize-space(.//a[contains(@href, "thanks.php")]/text())').extract())
            #if(len(item['like'])!=0):
            #print item['like']
            #if item.get('image','none') == 'none':
			#    item['image'] = 'https://d13yacurqjgara.cloudfront.net/users/370014/screenshots/1738726/teste-4-drble_1x.jpg';
            yield item
            
            
             

    