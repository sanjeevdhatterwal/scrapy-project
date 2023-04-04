import scrapy
#this spider scrapes the webpage and store that in html file
class quotes_spyder(scrapy.Spider):
    name="quotes_spider"
    def start_requests(self):
        urls=["http://quotes.toscrape.com/page/1/",
              "http://quotes.toscrape.com/page/2/",
              "http://quotes.toscrape.com/page/3/"
              ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        page=response.url.split("/")[-2]
        file_name="quotes-%s.html"%page
        with open(file_name,'wb') as file:
            file.write(response.body)
        self.log('saved file %s',file_name)
#this spider creates the json file of the above links
class spider_json(scrapy.Spider):
    name='json_spider'
    def start_requests(self):
        urls=["http://quotes.toscrape.com/page/1/",
              "http://quotes.toscrape.com/page/2/",
              "http://quotes.toscrape.com/page/3/"
              ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        page=response.url.split('/')[-2]
        for q in response.css("div.quote"):
            text=q.css('span.text::text').get()
            author=q.css('small.author::text').get()
            tags=q.css('a.tag::text').get()
            yield{
                'text':text,
                'author':author,
                'tags':tags
            }

#this spider will traverse all the pages that are associated with the given 
    
class spider_all(scrapy.Spider):
    name='all_spider'
    def start_requests(self):
        urls=['http://quotes.toscrape.com/page/1/']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self,response):
        page=response.url.split('/')[-2]
        for q in response.css("div.quote"):
            text=q.css('span.text::text').get()
            author=q.css('small.author::text').get()
            tags=q.css('a.tag::text').get()
            yield{
                'text':text,
                'author':author,
                'tags':q.css
            }
        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)
