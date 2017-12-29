#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/29 16:44
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce:
import redis
from task.decorator_task import singleton


@singleton
class RedisFactory(object):

    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379)
        self.redis_key = 'weixin_users'

    def hset(self, user_uuid, state):
        self.client.hset(self.redis_key, user_uuid, state)

    def hget(self, user_uuid):
        return self.client.hget(self.redis_key, user_uuid)


