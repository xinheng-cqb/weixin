#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/22 16:32
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 聊天机器人---小黄鸡调用
from mainMenu.string_util import StringUtil
import requests


class ChatRobot(object):
    cookie = ('dotcom_session_key=s%3A7gMTtW_Je6DVCaSVhAA2G7pMssHP6bQE.X1mWdP%2Fr0Okm%2BBIK6NLtdffzsjRSjP'
              'pwHGqOlJZI2''ws; _ga=GA1.2.475623500.1513929978; _gid=GA1.2.726369643.1513929978; lang=zh_CN; '
              'io=naUz2r89cVK0vrG''KAAAE; _gat_gtag_UA_21923282_1=1')

    def __init__(self):
        self.cooke_dict = StringUtil.parse_str_2_dict(self.cookie, '; ')

    def reply(self, text):
        url = 'http://www.simsimi.com/otn/talk?talkCnt=1&reqText={0}'.format(text)
        try_count = 0
        while try_count < 5:
            res = requests.get(url, cookies=self.cooke_dict)
            result = StringUtil.match_between_sign(res.text, r'sentence\\":\\"', r'\\"', 1)
            if result is not None:
                return result
            try_count += 1
        return '小脑瓜已过载，理解不了，换个词试试~~'

if __name__ == '__main__':
    print(ChatRobot().reply('日期'))
