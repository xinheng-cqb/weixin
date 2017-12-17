#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/17 16:06
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce:

import urllib
import json

from task.decorator_task import singleton


@singleton
class Basic(object):

    def __init__(self):
        self.access_token = ''

    def real_get_access_token(self):
        app_id = 'wx79516014049ad240'
        app_secret = 'dcc6d5e9458a9e869ca227c2203de758'
        post_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
                    "client_credential&appid={0}&secret={1}".format(app_id, app_secret))
        resp = urllib.urlopen(post_url)
        resp_json = json.loads(resp.read())
        self.access_token = resp_json['access_token']

    def get_access_token(self):
        return self.access_token
