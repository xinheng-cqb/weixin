#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/14 19:47
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 有道翻译API接口
import httplib
from hashlib import md5
import urllib
import random
import re
from mainMenu.string_util import StringUtil


class YouDaoTranslateAPI(object):
    def __init__(self):
        self.appKey = '6f2dc84c54c25bc4'
        self.secretKey = 'ptzWR0qV6439CrVJnpUQDxqQGV0SuEvp'

    def translate(self, word_text):
        http_client = None
        try:
            if isinstance(word_text, unicode):
                word_text = word_text.encode('utf-8')
            salt = random.randint(1, 65536)
            sign = self.appKey + word_text + str(salt) + self.secretKey
            m1 = md5()
            m1.update(sign)
            sign = m1.hexdigest()
            query_url = ('/api?appKey={0}&q={1}&salt={2}&sign={3}'
                         .format(self.appKey, urllib.quote(word_text), salt, sign))

            http_client = httplib.HTTPConnection('openapi.youdao.com')
            http_client.request('GET', query_url)
            response = http_client.getresponse()
            result = StringUtil.match_between_sign(response.read(), r'value":\[', '\]')
            if result is None:
                return '小子办不到,请输入正常点的内容~~'
            return result.replace(',', '\n')
        except Exception, e:
            print e
        finally:
            if http_client:
                http_client.close()

if __name__ == '__main__':
    str = u'正则表达式编译成对象'
    pattern = re.compile(u'[\u4e00-\u9fa5]+')
    matcher = re.search(pattern, str)
    if matcher:
        print matcher.group()