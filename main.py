#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/15 19:47
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce:

import web
from service.translateInter import TranslateInterface

urls = (
'/weixin','TranslateInterface'
)
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()