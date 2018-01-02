#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/17 16:29
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 异步任务

import threading
from task.scheduled_task import init_token, init_joke
import time


class MutilTask(object):

    @classmethod
    def invoke(cls):
        token_task = threading.Thread(target=init_token)
        token_task.start()
        time.sleep(2)  # 避免token未初始化前调用需要使用token的函数
        joke_task = threading.Thread(target=init_joke)
        joke_task.start()

if __name__ == '__main__':

    MutilTask().invoke()
