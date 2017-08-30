# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup

class IthomeSpider(scrapy.Spider):
    name = "ithome"

    custom_settings = {
        'COOKIES_ENABLED': False,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 0.5,
        'AUTOTHROTTLE_MAX_DELAY': 0.8,
        'DOWNLOAD_DELAY': 1.2,
    }

    def start_requests(self):
        yield scrapy.Request(
            "https://www.ithome.com/html/it/321659.htm",
            callback=self.generate_article_content
        )

    def generate_article_content(self, response):
        title = response.xpath('//div[@class="post_title"]/h1/text()').extract()
        print title
        time = response.xpath('//div//span[@id = "pubtime_baidu"]/text()').extract()
        print time
        source = response.xpath('//div//span[@id = "source_baidu"]/a/text()').extract()
        print source
        author = response.xpath('//div//span[@id = "author_baidu"]/strong/text()').extract()
        print author[0]
        editor = response.xpath('//div//span[@id = "editor_baidu"]/strong/text()').extract()
        print editor
        soup = BeautifulSoup(response.xpath('//div[@class="post_content"]').extract()[0], 'lxml')
        content = soup.get_text()
        print content


if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute('scrapy crawl ithome'.split())
