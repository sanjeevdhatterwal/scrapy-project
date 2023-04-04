import scrapy
class my_spider(scrapy.Spider):
    name="book_spider"
    def start_requests(self):
        urls=["http://books.toscrape.com/"]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        page=response.url.split('/')[-2]
        for q in response.css('article.product_pod'):
            name=q.css("h3 a::attr(title)").get()
            price=q.css("p.price_color::text").get()
            yield{
                'name':name,
                'price':price,
            }
        next_page=response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

