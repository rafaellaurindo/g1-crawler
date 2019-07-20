# -*- coding: utf-8 -*-
import scrapy
from G1Crawler.items import G1CrawlerItem


class G1spiderSpider(scrapy.Spider):
    name = 'G1Spider'
    allowed_domains = ['g1.globo.com']
    start_urls = ['https://g1.globo.com/economia/tecnologia',
                  'https://g1.globo.com/educacao/']

    def parse(self, response):
        for notice in response.css(".bastian-page .bastian-feed-item"):
            title = notice.css('a::text').extract_first()
            time = notice.css('.feed-post-datetime::text').extract_first()
            description = notice.css(
                '.feed-post-body-resumo div::text').extract_first()
            link = notice.css('a::attr(href)').extract_first()

            notice_item = G1CrawlerItem(
                title=title,
                time=time,
                description=description,
                link=link,
            )
            yield notice_item
