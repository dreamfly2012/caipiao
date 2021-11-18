# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    periods = scrapy.Field()
    nums1 = scrapy.Field()
    nums2 = scrapy.Field()
    nums3 = scrapy.Field()
    pass
