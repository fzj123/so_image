# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request


class ImagesSpider(scrapy.Spider):
    name = "images"
    BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
    start_index = 0
    MAX_DOWNLOAD_NUM = 1000
    start_urls = [BASE_URL % 0]

    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))
        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}
        self.start_index += infos['count']
        print('测试数据%s' % self.start_index)
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield Request(self.BASE_URL % self.start_index)




