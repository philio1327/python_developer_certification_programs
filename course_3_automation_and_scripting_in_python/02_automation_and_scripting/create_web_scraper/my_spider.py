import scrapy

# to run this and make it work
# Open Command Prompt and navigate to this folder "create_web_scraper"
# you can also use VS Code's terminal or Pycharm's terminal. They both work!
# input the following commands (hit ENTER after each)
# cd venv
# cd Scripts
# activate
# cd .../
# cd my_spider
# cd my_spider
# cd spiders
# scrapy crawl my_spider

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ["https://www.yahoo.com/"]

    def parse(self, response):
        yield{
            'title': response.css('title::text').get(),
            'paragraphs':response.css('p::text').getall()
        }