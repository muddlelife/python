# -*- coding:utf-8 -*-
import requests  # 导入网页爬取模块
import re  # 导入re模块
from xml import etree

class wallhave_picture(object):
    """
    爬取网站https://wallhaven.cc/的照片
    """
    def __init__(self, part_url):
        self.url = 'https://wallhaven.cc/' + part_url
        self.header = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 "
            "Safari/537.36 SE 2.X MetaSr 1.0"
        }

    def request(self):
        response = requests.get(self.url, headers=self.header).text
        return response

    def parse(self, response):
        html = etree.HTML(response)

        picture_url = html.xpath('//*[@id="thumbs"]/section[1]/ul/li/figure/a/@href')
        print(picture_url)



if __name__ == '__main__':

    part_url = input('请输入一个类别')

    dongman = wallhave_picture(part_url)
    html = dongman.request()
    dongman.parse(html)
