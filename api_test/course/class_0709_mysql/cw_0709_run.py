#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: test_cw0625_run_log_1.py
@Time: 2019-06-29 22:19
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
from interface_automation.class_0709_mysql import HTMLTestRunnerNew
from interface_automation.class_0709_mysql.cw_0709_case_suite import suite

with open('test_resule.html', 'wb')as save_file:
    result = HTMLTestRunnerNew.HTMLTestRunner(stream=save_file, verbosity=2, title='四则运算测试用例报告',
                                              description='测试两数的四则运算',
                                              tester='刀刀')
    result.run(suite)
