import scrapy

base = 'https://baomoi.com/x/c/'
class NewsSpider(scrapy.Spider):
    name = 'news'
    id1=id2=40985601
    count = 0;
    num_page=1;
    def start_requests(self):
    	while self.count < 10000:
    		yield scrapy.Request(base+str(self.id1)+".epi")
    		self.id1+=1
    		self.id2-=1
    		yield scrapy.Request(base+str(self.id2)+".epi")
    		


    def parse(self, response):
    	a=str(response)
    	if(len(base) < len(a) - 5):
    		self.count+=1
    		a = "null"
    		if len(response.css('.bm_Bk > a > span').getall()) != 0: 
    			a=response.css('.bm_Bk > a > span').getall()[1][6:-7]
    		yield {
    			"title" : response.css('title::text').get(),
    			"overview" : response.css('.bm_AQ.bm_P::text').get(),
    			"source" : a
    		}	
    	
    	

    	
