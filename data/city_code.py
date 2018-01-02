#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2018/1/2 9:16
# @Author  : xinheng-cqb
# @Software: PyCharm Community Edition
# @introduce: 城市编码
import os

from task.decorator_task import singleton


@singleton
class CityCode(object):

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.city_code_root = os.path.join(self.app_root, '..', 'profile/city_code.txt')
        self.filter_char_list = ['县', '区', '市', '省']  # 要求级别从低到高排序
        self.city_code_dict = {}

    def loading(self):
        with open(self.city_code_root, 'rb') as file:
            line = file.readline()
            while line:
                temp_arr = line.split('=')
                self.city_code_dict[temp_arr[-1].replace('\r\n', '')] = temp_arr[0]
                line = file.readline()

    def get_code_code(self, city_name):
        if len(self.city_code_dict) < 10:
            self.loading()
        city_code = self.city_code_dict.get(city_name)
        if city_code is None:
            city_name = self.filter_city_name(city_name)
            city_code = self.city_code_dict.get(city_name)
        return city_code

    def filter_city_name(self, city_name):
        for filter_char in self.filter_char_list:
            city_name_arr = city_name.split(filter_char)
            if len(city_name_arr) == 1:
                continue
            elif city_name_arr[-1] == '':
                city_name = city_name_arr[0]
            else:
                city_name = self.filter_city_name(city_name_arr[-1])
        return city_name


if __name__ == '__main__':
    print CityCode().get_code_code('浙江省杭州市苍南县')