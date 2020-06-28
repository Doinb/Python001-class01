import scrapy
from ..items import MaoyanItem
from scrapy.selector import Selector


class MaoyanMovieSpider(scrapy.Spider):
    name = 'maoyan_movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=3']

    def start_requests(self):
        url = "https://maoyan.com/films?showType=3&sortId=3&offset=0"
        yield scrapy.Request(url, callback=self.parse, dont_filter=True)


    def parse(self, response):
        movies = Selector(response=response).xpath("//div[@class='movie-hover-info']")
        for movie in movies[0:10]:
            item = MaoyanItem()
            name = movie.xpath('./div[1]/span/text()').extract()[0].strip('\n').strip()
            tags = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
            release_time = movie.xpath('./div[last()]/text()').extract()[1].strip('\n').strip()
            item.update({'name': name, 'tags': tags, 'release_time': release_time})
            yield item

