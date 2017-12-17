#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/14 9:48
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce:
import hashlib
import web
import os


class WeixinInterface(object):
    app_root = os.path.dirname(__file__)
    templates_root = os.path.join(app_root, '..', 'templates/')
    render = web.template.render(templates_root)

    def __init__(self):
        pass

    def GET(self):
        # 获取输入参数
        data = web.input()
        if len(data) == 0:
            return "hello, this is handle view"
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echo_str = data.echostr

        # 自己的token
        token = "xinheng_weixin"
        # 字典序排序
        param_list = [token, timestamp, nonce]
        param_list.sort()
        # sha1加密算法
        sha1 = hashlib.sha1()
        map(sha1.update, param_list)
        hashcode = sha1.hexdigest()

        # 如果是来自微信的请求，则回复echo_str
        if hashcode == signature:
            return echo_str