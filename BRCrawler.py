import scrapy
from scrapy.crawler import CrawlerProcess

class TedSpiderBr(scrapy.Spider):
    name = "ted_spider_br"
    download_delay = 0.5

    def start_requests(self):
        for url in urls_list_br:
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
        talk = talk.replace('\n',' ')
        ted_dict[title] = talk
        
urls_list_br = ['https://www.ted.com/talks?sort=newest&language=pt-br']
for i in range(2,97):
    urls_list_br.append('https://www.ted.com/talks?language=pt-br&page='+str(i)+'&sort=newest')


# Initialize the dictionary **outside** of the Spider class
ted_dict_br = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(TedSpiderBr)
process.start()

with open('br_dict.csv', 'w', encoding='utf-8') as f:
    for key in ted_dict.keys():
        f.write("%s;%s\n"%(key,ted_dict[key]))