import scrapy, json

from architectureDaily.items import ArchitecturedailyItem
from pprint import pprint



class ArchitectureSpider(scrapy.Spider):


    json_data=open('C:\\Python27\\Scripts\\architectureDaily\\architectureDaily\\threads.json').read()
    data = json.loads(json_data) 
   
    name = "get_posts"
    allowed_domains = ["skyscrapercity.com"]
    
 
  
        
    def start_requests(self):
        for item in self.data: 
            print('http://www.skyscrapercity.com/'+item['link'])
            yield scrapy.Request('http://www.skyscrapercity.com/'+item['link'], self.parse)

         
    def parse(self, response):        
        item = ArchitecturedailyItem()  
        for post in response.xpath('//td[contains(@id, "td_post")]'):        
            item['id'] = ''.join(post.xpath('normalize-space(@id)').extract())
            #item['title'] = sel.xpath('normalize-space(div[contains(@id, "post_message")]/text() | div[contains(@id, "post_message")]//*/text())').extract()
            item['title'] = ''.join(post.xpath('normalize-space(div[contains(@id, "post_message")]/text())').extract())
            item['image'] = post.xpath('normalize-space(div[contains(@id, "post_message")]/img/@src)').extract_first()
            item['like'] = ''.join(post.xpath('normalize-space(.//a[contains(@href, "thanks.php")]/text())').extract())
        '''    
        item['city'] = response.xpath('normalize-space(//meta[@name="keywords"]/@content)').extract_first().split(",")[0]
        print("city")
        print(item['city'])   
      '''
        yield item
         
         
