#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/15 19:47
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce:

import web
from service.wei_xin_handle import WeiXinHandle
from task.mutil_task import MutilTask

urls = (
'/weixin','WeiXinHandle'
)
if __name__ == '__main__':
    MutilTask().invoke()
    app = web.application(urls, globals())
    app.run()