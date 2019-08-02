#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: eureka_path.py
@Time: 2019-08-03 00:18
@Desc: Eureka
"""
import os

# 获取项目根目录
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_TEST_DIR = os.path.join(PROJECT_DIR, 'api_test')
API_TEST_ARCHITECTURE_DIR = os.path.join(API_TEST_DIR, 'architecture')
API_TEST_ARCHITECTURE_SCRIPT_DIR = os.path.join(API_TEST_ARCHITECTURE_DIR, 'script')

if __name__ == '__main__':
    print(PROJECT_DIR)
    print(API_TEST_DIR)
    print(API_TEST_ARCHITECTURE_DIR)
    print(API_TEST_ARCHITECTURE_SCRIPT_DIR)
