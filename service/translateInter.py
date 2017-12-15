#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/14 19:32
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce:
from mainMenu.utilMenu.translate import YouDaoTranslateAPI
from service.weixinInter import WeixinInterface
from lxml import etree
import web
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TranslateInterface(WeixinInterface):
    def __init__(self):
        super(WeixinInterface, self).__init__()
        self.trans_api = YouDaoTranslateAPI()

    def POST(self):
        str_xml = web.data()
        xml = etree.fromstring(str_xml)
        msg_type = xml.find('MsgType').text
        from_user = xml.find("FromUserName").text
        to_user = xml.find("ToUserName").text
        if msg_type == 'text':
            content = xml.find("Content").text
            return self.render.reply_text(from_user, to_user, int(time.time()), self.trans_api.translate(str(content)))

if __name__ == '__main__':
    t = u'消费记录'
    print str(t)
    t = TranslateInterface()
    print t.trans_api.translate('消费记录')