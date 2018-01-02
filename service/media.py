#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/29 19:49
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce:
from basic import Basic
import urllib2
import poster.encode
from poster.streaminghttp import register_openers
import requests
import os
import json
from task.decorator_task import singleton


@singleton
class Media(object):
    def __init__(self):
        register_openers()

    def upload_with_url(self, url, media_type='image'):
        res = requests.get(url, stream=True)
        temp_file_name = url.split('/')[-1]
        with open(temp_file_name, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)
        media_id = self.uplaod(temp_file_name, media_type)
        os.remove(temp_file_name)
        return media_id

    def uplaod(self, file_name, media_type='image'):
        file = open(file_name, "rb")
        param = {'media': file}
        post_data, post_headers = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (
            Basic().get_access_token(), media_type)
        request = urllib2.Request(postUrl, post_data, post_headers)
        urlResp = urllib2.urlopen(request)
        info_json = json.loads(urlResp.read())
        return info_json['media_id']


if __name__ == '__main__':
    s = 'http://juheimg.oss-cn-hangzhou.aliyuncs.com/joke/201705/10/0C76921F3009B1CD4636C13C69D31F2F.jpg'
    Basic().real_get_access_token()
    print Media().upload_with_url(s)
