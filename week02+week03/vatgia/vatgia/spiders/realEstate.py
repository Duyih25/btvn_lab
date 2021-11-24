import scrapy

base = 'https://vatgia.com/api/v2/raovat/filter?cat_id=2588&page={}&max_timestamp=1637685239&sort=0'
class RealestateSpider(scrapy.Spider):
    name = 'realEstate'
    start_urls = [base.format(1)]

    count = 0;
    def parse(self, response):
        house = response.json()
        #print(house["success"])
        
        for product in house['data']["products"]:
        	self.count+=1
        	tmp = product['poster_address'].find('</i>')
        	yield {
        		'house overview' : product['name'],
        		'host' : product['poster_name'],
        		'location' : product['poster_address'][tmp+4:]
        	}
        if self.count < 5000:
        	next_page = house['data']['nextpage']	
        	next_page_url = base.format(next_page);
        	yield scrapy.Request(next_page_url)
