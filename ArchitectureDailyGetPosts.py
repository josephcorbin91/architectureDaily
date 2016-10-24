import scrapy, json

from architectureDaily.items import ArchitecturedailyItem



class ArchitectureSpider(scrapy.Spider):


    json_data=open(file_directory).read()
    data = json.loads(json_data)
    pprint(data)
    
    
    
    city="London"
    name = "get_posts"
    allowed_domains = ["skyscrapercity.com"]
    start_urls = ["http://www.skyscrapercity.com/showthread.php?t=1697283&page=7"] 
    nPage = 1
    

    def parse(self, response):
        global nPage
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
            
            """
            To scrape mutliple pages 
        next_page = response.xpath('//a[@rel="prev"]/@href').extract_first()

        
        print('nextpage')
        print(next_page)
        print('npage first')
        print(nPage)
        if next_page is not None and nPage != 5:
            next_page = response.urljoin(next_page)
            nPage+=1
            print('npage second')
            print(nPage)
            yield scrapy.Request(next_page, callback=self.parse)
           """