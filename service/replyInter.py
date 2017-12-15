#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/14 20:11
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 自动回答接口
from service.weixinInter import WeixinInterface
import time
from lxml import etree
import web


class ReplyInterface(WeixinInterface):
    def __init__(self):
        super(WeixinInterface, self).__init__()

    def POST(self):
        str_xml = web.data()
        xml = etree.fromstring(str_xml)
        msg_type = xml.find('MsgType').text
        from_user = xml.find("FromUserName").text
        to_user = xml.find("ToUserName").text

        if msg_type == 'event':
            msg_content = xml.find('Event').text
            if msg_content == 'subscribe':  # 关注的时候的欢迎语
                return self.render.reply_text(from_user, to_user, int(time.time()), "白茶清欢无别事，我在等风也等你~~")
            elif msg_content == 'unsubscribe':
                return self.render.reply_text(from_user, to_user, int(time.time()), "人生若只如初见，铭记都是好印象！！！")


        if msg_type == 'text':
            content = xml.find("Content").text
            if content == 'help':
                return self.render.reply_text(from_user, to_user, int(time.time()), "随便看看？（对不起我功能有限...）")
            else:
                return self.render.reply_text(from_user, to_user, int(time.time()), "哎呀出错了 输入个help看看如何正确的调戏我？")