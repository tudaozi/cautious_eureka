#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: cw_0706_request.py
@Time: 2019-07-08 01:01
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
import json

import requests

from interface_automation.class_0709_mysql.cw_0709_config import do_config
from interface_automation.class_0709_mysql.cw_0709_log import do_logger


class HttpRequest:
    def __init__(self):
        self.one_session = requests.Session()

    def send_request(self, method, url, data=None, is_json=False, **kwargs):
        method = method.upper()
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                do_logger.error("将json转为Python中的数据类型时, 出现异常: {}".format(e))
                data = eval(data)
        if method == 'GET':
            res = self.one_session.request(method=method, url=url, params=data, **kwargs)
        elif method == 'POST':
            if is_json:
                res = self.one_session.request(method=method, url=url, json=data, **kwargs)
            else:
                res = self.one_session.request(method=method, url=url, data=data, **kwargs)
        else:
            res = None
            do_logger.error("不支持【{}】方法请求".format(method))
        return res

    def request_close(self):
        self.one_session.close()


do_request = HttpRequest()

if __name__ == '__main__':
    # url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/register'
    # params = {
    #     'mobilephone': 13798288888,
    #     'pwd': 123456,
    #     'regname': '刀刀'
    # }
    # my_httprequest = HttpRequest()
    # my_httprequest.send_request(method='GET', url=url, data=params)

    case_list = {'case_id': 1, 'title': '使用不存在的手机号进行注册', 'url_path': '/member/register',
                 'data': '{"mobilephone": "13786245301", "pwd": 123456, "regname": "刀刀"}', 'method': 'POST',
                 'expected': 'code: "10001",', 'actual': None, 'result': None}

    actual = do_request.send_request(method=case_list['method'],
                                     url=do_config.get_value('request', 'default_address') + case_list['url_path'],
                                     data=eval(case_list['data']))
