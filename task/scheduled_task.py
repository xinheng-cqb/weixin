#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/9 11:38
# @Author  : Qibin Cai
# @Software: PyCharm Community Edition
# @introduce: 定时任务,通过装饰器来实现可配置
import time

from service.basic import  Basic
from task.decorator_task import scheduled_task


@scheduled_task(1.9)
def init_token():
    Basic().real_get_access_token()

