# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ThetoletItem(scrapy.Item):
    title = scrapy.Field()
    basic_info = scrapy.Field()
    address = scrapy.Field()
    price_per_month = scrapy.Field()
    type = scrapy.Field()
    purpose = scrapy.Field()
    amenities = scrapy.Field()
    description = scrapy.Field()
    price_negotiable = scrapy.Field()
    property_url = scrapy.Field()
