#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/18 19:06
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 对客户端接受到的内容进行相应的包装
import xml.etree.ElementTree as ET


def parse_xml(web_data):
    if len(web_data) == 0:
        return None
    xml_data = ET.fromstring(web_data)
    msg_type = xml_data.find('MsgType').text
    if msg_type == 'text':
        return TextMsg(xml_data)
    elif msg_type == 'image':
        return ImageMsg(xml_data)
    elif msg_type == 'event':
        event_type = xml_data.find('Event').text
        if event_type == 'CLICK':
            return Click(xml_data)
        elif event_type in ('subscribe', 'unsubscribe'):
            return Subscribe(xml_data)
        #elif event_type == 'VIEW':
            #return View(xmlData)
        #elif event_type == 'LOCATION':
            #return LocationEvent(xmlData)
        #elif event_type == 'SCAN':
            #return Scan(xmlData)


class Base(object):
    def __init__(self, xml_data):
        self.to_user_name = xml_data.find('ToUserName').text
        self.from_user_name = xml_data.find('FromUserName').text
        self.create_time = xml_data.find('CreateTime').text
        self.msg_type = xml_data.find('MsgType').text


class Msg(Base):
    def __init__(self, xml_data):
        Base.__init__(self, xml_data)
        self.msg_id = xml_data.find('MsgId').text


class TextMsg(Msg):
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.content = xml_data.find('Content').text.encode("utf-8")


class ImageMsg(Msg):
    def __init__(self, xml_data):
        Msg.__init__(self, xml_data)
        self.pic_url = xml_data.find('PicUrl').text
        self.media_id = xml_data.find('MediaId').text


class EventMsg(Base):
    def __init__(self, xml_data):
        Base.__init__(self, xml_data)
        self.event = xml_data.find('Event').text


class Click(EventMsg):
    def __init__(self, xml_data):
        EventMsg.__init__(self, xml_data)
        self.event_key = xml_data.find('EventKey').text


class Subscribe(EventMsg):
    def __init__(self, xml_data):
        EventMsg.__init__(self, xml_data)

    def reply_text(self):
        if self.event == 'subscribe':  # 关注的时候的欢迎语
            return '白茶清欢无别事，我在等风也等你~~'
        elif self.event == 'unsubscribe':
            return '人生若只如初见，铭记都是好印象！！！'