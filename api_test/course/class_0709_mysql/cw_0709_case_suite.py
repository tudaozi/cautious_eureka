#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: test_cw0625_case_suite_1.py
@Time: 2019-06-29 22:19
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
import unittest

from interface_automation.class_0709_mysql.cw_0709_case import ApiTest

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(ApiTest))

if __name__ == '__main__':
    unittest.main()
