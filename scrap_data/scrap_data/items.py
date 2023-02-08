# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapDataItem(scrapy.Item):
    # define the fields for your item here like:
    product = scrapy.Field()
    sale = scrapy.Field()
    unit = scrapy.Field()
    _id = scrapy.Field()
