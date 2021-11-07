import scrapy

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
            yield{
                    "periods":td[0].css("::text").get(),
                    "nums1":td[1].css("::text").get(),
                    "nums2":td[2].css("::text").get(),
                    "nums3":td[3].css("::text").get()
                    }
        pass
