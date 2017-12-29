#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/28 20:25
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 聚合数据笑话API （免费, 可以聚合数据上申请，每天有调用上限）
import time
import requests
import json
from task.decorator_task import singleton


@singleton
class JokeAPI(object):
    _AppKey = '6ed6fa1e904acdf96d3bafb8adfff756'

    def __init__(self):
        self.content_list = []
        self.pic_dict = {}

    def acquire_content_list(self, page_count=5):
        self.content_list.clear()
        hash_set = set('')
        current_time_stamp = int(time.time())
        try:
            for page in range(1, page_count + 1):
                url = 'http://japi.juhe.cn/joke/content/list.from?key={0}&page={1}&pagesize=20&sort=desc&time={2}'.format(
                    self._AppKey, page, current_time_stamp)
                res = requests.get(url)
                info_json = json.loads(res.text)
                data = info_json['result']['data']
                for each in data:
                    hash_id = each['hashId']
                    if hash_id in hash_set:
                        continue
                    hash_set.add(hash_id)
                    self.content_list.append(each['content'])
        except Exception as e:
            print(e)

    def acquire_pic_dict(self, page_count=5):
        self.pic_dict.clear()
        hash_set = set('')
        current_time_stamp = int(time.time())
        try:
            for page in range(1, page_count + 1):
                url = 'http://japi.juhe.cn/joke/img/list.from?key={0}&page={1}&pagesize=20&sort=desc&time={2}'.format(
                        self._AppKey, page, current_time_stamp)
                res = requests.get(url)
                info_json = json.loads(res.text)
                data = info_json['result']['data']
                for each in data:
                    hash_id = each['hashId']
                    if hash_id in hash_set:
                        continue
                    hash_set.add(hash_id)
                    self.pic_dict[each['url']] = each['content']
        except Exception as e:
            print(e)

    def invoke_acquire(self, page_count=5):
        self.acquire_content_list(page_count)
        self.acquire_pic_dict(page_count)

    def get_content_list(self):
        return self.content_list

    def get_pic_dict(self):
        return self.pic_dict

if __name__ == '__main__':
    JokeAPI().invoke_acquire(1)
    result = JokeAPI().get_content_list()
    print(len(result))
