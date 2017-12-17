#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/17 16:58
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce:
from functools import wraps
import time


def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return get_instance


def scheduled_task(hours, cyclic=True):
    def _scheduled_task(func):
        def __scheduled_task(*args):
            time_count = 1
            while cyclic or time_count == 1:
                print ('{0} scheduled_task is start, time_{1}'.format(func.func_name, time_count))
                func(*args)
                print('{0} scheduled_task is end, time_{1}'.format(func.func_name, time_count))
                time.sleep(60 * 60 * hours)
                time_count += 1
        return __scheduled_task
    return _scheduled_task
