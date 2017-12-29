#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2017/12/14 16:21
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 常用工具类
import re
import datetime


class StringUtil(object):
    def __init__(self):
        pass

    @staticmethod
    def tran_scientific_notation(num):
        if num.find('E') > 0:
            num = float(num.split('E')[0]) * 10000000
        return num

    @staticmethod
    def match_between_sign(text, prefix, suffix, index=0, suffix_more_char=False):
        pattern = re.compile(prefix + r'([^' + suffix + ']+)')
        if suffix_more_char:
            pattern = re.compile(prefix + r'(.*?)' + suffix)
            index = 0
        match = re.findall(pattern, text)
        if len(match) > 0:
            return match[index]
        else:
            return None

    @staticmethod
    def match_number(text, sign, index=0):
        pattern = re.compile(sign + r'([-E\d.]+)')
        match = re.findall(pattern, text)
        if len(match) > 0:
            return match[index]
        else:
            return None

    @staticmethod
    def parse_str_2_dict(str_info, split_sign='&'):
        info_dict = {}
        for param in str_info.split(split_sign):
            index = param.index('=')
            info_dict[param[0:index]] = param[index + 1:]
        return info_dict

    @staticmethod
    def get_before_date(age, month=0, day=0, format='%Y-%m-%d'):
        now = datetime.datetime.now()
        if month < 1 or month > 12:
            month = now.month
        if day < 1 or day > 31:
            day = now.day
        return datetime.date(now.year - age, month, day).strftime(format)
