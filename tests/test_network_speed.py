#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 12/7/19 4:53 PM
# @Author : xuezhi.zhang
# @File : test_network_speed.py
import sys
sys.path.append('.')
sys.path.append('..')
from network.speed import get_ping_time


def _test_ping_time():
    print("============== 测试 Ping Time =============")
    ping_time = get_ping_time("www.baidu.com")
    print("www.baidu.com >> %sms" % ping_time)
    ping_time = get_ping_time("127.0.0.1")
    print("127.0.0.1 >> %sms" % ping_time)


if __name__ == "__main__":
    _test_ping_time()
