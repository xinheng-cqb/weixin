#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/17 16:29
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 异步任务

import threading
from task.scheduled_task import init_token


class MutilTask(object):

    @classmethod
    def invoke(cls):
        token_task = threading.Thread(target=init_token)
        token_task.start()

if __name__ == '__main__':

    MutilTask().invoke()
