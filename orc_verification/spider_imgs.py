#!/usr/share/app/anaconda3/bin/python3
# encoding: utf-8
import time

import requests
import user_agent
from utils.tools import primary_md5

from setting import project_path

""" 
@version: v1.0 
@author: pu_yongjun

这个脚本是用来爬取验证码的一个脚本

目标网站：http://xinhua.qudaba.com

单张图片爬取，没有采用批量的方式
"""


class SpiderImg(object):
    """ 这个类就是用来爬取验证码
    """

    def __init__(self, img_nums):
        """
        url 是验证码的地址
        """
        self.url = 'http://xinhua.qudaba.com/search/getVerify'
        self.img_nums = img_nums
        self.img_path = project_path + '/captcha/other_img'

    def start_spider(self):
        """ 这个函数是用来启动爬取任务的函数
        :return:
        """
        for line in range(0, self.img_nums):
            img_names = primary_md5()
            headers = {
                'user-agent': user_agent.base.generate_user_agent()
            }
            resp = requests.get(url=self.url, headers=headers)
            file_path = self.img_path + '/' + img_names + '.jpg'
            with open(file_path, 'wb') as f:
                f.write(resp.content)

            time.sleep(2)


if __name__ == '__main__':
    s = SpiderImg(img_nums=100)
    s.start_spider()
