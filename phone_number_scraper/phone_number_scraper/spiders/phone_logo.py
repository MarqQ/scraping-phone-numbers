import re
import os
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PhoneAndLogoSpider(CrawlSpider):
    name = "phones"
    allowed_domains = ["mossyford.com"]
    start_urls = ["https://www.mossyford.com/"]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        phones = re.findall(r'[(][\d]{3}[)]\s[\d]{3}-[\d]{4}', response.text)
        for phone in phones:
            if 'boostrap' not in phone:
                yield {
                    'phone': phone,
                    'link': response.url
                }
            os.system("scrapy runspider \scraping-phone-numbers\phone_number_scraper\phone_number_scraper\spiders"
                      "\phone_logo.py -O phones.json")
