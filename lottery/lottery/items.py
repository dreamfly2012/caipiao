# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    period = scrapy.Field()
    num1 = scrapy.Field()
    num2 = scrapy.Field()
    num3 = scrapy.Field()

    pass
