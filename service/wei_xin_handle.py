#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/14 9:48
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce:
import hashlib
import web
import os

from data.redis_factory import RedisFactory
from mainMenu.utilMenu.chat_robot import ChatRobot
from mainMenu.utilMenu.joke import JokeAPI
from mainMenu.utilMenu.translate import YouDaoTranslateAPI
from service import receive
import time


class WeiXinHandle(object):
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, '..', 'templates/')
        self.render = web.template.render(self.templates_root)
        pass

    def GET(self):
        # 获取输入参数
        web_data = web.input()
        print('-------- WeiXin Handle Post web_data is:\n{0}'.format(web_data))
        if not hasattr(web_data, 'signature'):
            return "hello, this is handle view"
        signature = web_data.signature
        timestamp = web_data.timestamp
        nonce = web_data.nonce
        echo_str = web_data.echostr

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

    def POST(self):
        try:
            web_data = web.data()
            print('WeiXin Handle Post web_data is:\n{0}'.format(web_data))  # 后台打日志
            rec_msg = receive.parse_xml(web_data)
            if isinstance(rec_msg, receive.TextMsg):
                if rec_msg.content == 'help':
                    return self.render.reply_text(rec_msg.from_user_name, rec_msg.to_user_name, int(time.time()),
                                                  'lt-->开启聊天模式\nfy-->开启翻译模式\nqt-->查看搞笑趣图\ndz-->查看有趣段子')
                elif rec_msg.content == 'lt':
                    RedisFactory().hset(rec_msg.from_user_name, 'lt')
                    return self.render.reply_text(rec_msg.from_user_name, rec_msg.to_user_name, int(time.time()),
                                                  '已切换到聊天模式 >_<')
                elif rec_msg.content == 'fy':
                    RedisFactory().hset(rec_msg.from_user_name, 'fy')
                    return self.render.reply_text(rec_msg.from_user_name, rec_msg.to_user_name, int(time.time()),
                                                  '已切换到翻译模式 ~~')
                elif rec_msg.content == 'dz':
                    return self.render.reply_text(rec_msg.from_user_name, rec_msg.to_user_name, int(time.time()),
                                                  '\n\n'.join(JokeAPI().get_content_list_random()))
                elif rec_msg.content == 'qt':
                    key, value = JokeAPI().get_pic_dict_random()
                    return self.render.reply_image(rec_msg.from_user_name, rec_msg.to_user_name, int(time.time()),
                                                   value, key)

                if RedisFactory().hget(rec_msg.from_user_name) == 'lt':
                    return self.render.reply_text(rec_msg.from_user_name, rec_msg.to_user_name, int(time.time()),
                                                  ChatRobot().reply(str(rec_msg.content)))
                return self.render.reply_text(rec_msg.from_user_name, rec_msg.to_user_name, int(time.time()),
                                              YouDaoTranslateAPI().translate(str(rec_msg.content)))

            if isinstance(rec_msg, receive.ImageMsg):
                return ''
            if isinstance(rec_msg, receive.Click):
                return ''
            if isinstance(rec_msg, receive.Subscribe):
                reply_text = rec_msg.reply_text()
                return self.render.reply_text(rec_msg.from_user_name, rec_msg.to_user_name, int(time.time()),
                                              reply_text)
            print("暂且不处理")
            return '功能还在开发中'
        except Exception as e:
            print(e)
