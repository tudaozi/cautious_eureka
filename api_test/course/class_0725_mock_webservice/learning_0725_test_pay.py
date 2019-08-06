#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: learning_0725_test_pay.py
@Time: 2019-08-07 01:17
@Desc: Eureka
"""
import unittest
from unittest import mock
from .learning_0725_payment import Payment


class PaymentTest(unittest.TestCase):
    """
    测试支付接口
    """

    def setUp(self):
        self.payment = Payment()

    def test_01_success(self):
        """
        测试支付成功
        :return:
        """
        self.payment.auth = mock.Mock(return_value=200)
        res = self.payment.pay(user_id=1001, card_num=12345, amount=500000)
        self.assertEqual("success", res)

    def test_02_fail(self):
        """
                测试支付失败
                :return:
                """
        self.payment.auth = mock.Mock(return_value=500)
        res = self.payment.pay(user_id=1001, card_num=12345, amount=500000)
        self.assertEqual("Fail", res)


if __name__ == "__main__":
    unittest.main()
