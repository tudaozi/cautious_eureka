#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: cw0625_testing_object.py
@Time: 2019-06-29 21:48
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""


class Arithmetic:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def add(self):
        return self.first_num + self.second_num

    def minus(self):
        return self.first_num - self.second_num

    def multiply(self):
        return self.first_num * self.second_num

    def division(self):
        try:
            result = self.first_num / self.second_num
            return round(result, 2)
        except ZeroDivisionError:
            return '∞'
