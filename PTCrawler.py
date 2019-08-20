import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess

class TedSpiderPt(scrapy.Spider):
    name = "ted_spider_pt"
    
    download_delay = 0.5

    def start_requests(self):
        for url in urls_list_pt:
            yield scrapy.Request(url=url,
                                 callback=self.parse_front)

    # First, parse links to talks and add transcript

    def parse_front(self, response):
        talk_links = response.css("a.ga-link::attr(href)")
        links_to_follow = talk_links.extract()
        for url in links_to_follow:
            url = url.replace('?language', '/transcript?language')
            yield response.follow(url=url,
                                  callback=self.parse_pages)
    # Second parsing method:

    def parse_pages(self, response):
        # Create a SelectorList of the talk
        title = response.xpath('//head/title/text()').extract_first()
        title = title.strip()
        title = title.split(':')[0]
        talk = response.xpath(
            '//div[@class="Grid__cell flx-s:1 p-r:4"]/p/text()').extract()
        for line in talk:
            line = line.strip()
            line = line.replace('\n',' ')
            line = line.replace('\t',' ')
        talk = '  '.join(talk)
        ted_dict[title] = talk

urls_list_pt = ['https://www.ted.com/talks?sort=newest&language=pt']
for i in range(2,79):
    urls_list_pt.append('https://www.ted.com/talks?language=pt&page='+str(i)+'&sort=newest')

# Initialize the dictionary **outside** of the Spider class
ted_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(TedSpiderPt)
process.start()

talks_pt = pd.DataFrame.from_dict(ted_dict, orient='index')

talks_pt.to_excel('talks_pt.xlsx')