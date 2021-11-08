import scrapy
from lottery.items import LotteryItem

class LotterySpider(scrapy.Spider):
    name = "lottery"

    start_urls = [
            'https://zst.cjcp.com.cn/cjw3d/view/3d_danxuan_content.html'
            ]

    def parse(self, response):
        print("parse data...")
        data = response.css('#pagedata')

        for tr in data.css("tr"):
            td = tr.css("td")
            item = LotteryItem()
            nums = td[3].css("::text").get()
            item["period"]=td[1].css("::text").get()
            item["num1"]= nums[0:1]
            item["num2"]= nums[1:2]
            item["num3"]= nums[2:3]
            yield item
        pass
