#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/28 20:25
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 聚合数据笑话API （免费, 可以聚合数据上申请，每天有调用上限）
import time
import requests
import json
import random

from service.basic import Basic
from service.media import Media
from task.decorator_task import singleton


@singleton
class JokeAPI(object):
    _AppKey = '6ed6fa1e904acdf96d3bafb8adfff756'

    def __init__(self):
        self.content_list = []
        self.pic_dict = {}

    def acquire_content_list(self, page_count=5):
        self.content_list=[]
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
                    media_id = Media().upload_with_url(each['url'])
                    self.pic_dict[media_id] = each['content']
        except Exception as e:
            print(e)

    def invoke_acquire(self, page_count=5):
        self.acquire_content_list(page_count)
        self.acquire_pic_dict(page_count)

    def get_content_list_random(self):
        a, b = random.randint(0, len(self.content_list)), random.randint(0, len(self.content_list))
        result_list = [self.content_list[a], self.content_list[b]]
        return result_list

    def get_pic_dict_random(self):
        a= random.randint(0, len(self.pic_dict))
        key_list = self.pic_dict.keys()
        key_a = key_list[a]
        return key_a, self.pic_dict.get(key_a)

if __name__ == '__main__':
    Basic().real_get_access_token()
    JokeAPI().invoke_acquire(1)
    result = JokeAPI().get_content_list_random()
    print(len(result))
