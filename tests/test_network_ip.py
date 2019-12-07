#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 12/7/19 4:51 PM
# @Author : xuezhi.zhang
# @File : test_network_ip.py
import sys
sys.path.append('.')
sys.path.append('..')
from network.ip import get_ip_info, get_ip_public, domain2ip, is_ip


def _test_get_ip_info():
    print("============== 测试 获取公网IP 和 获取公网IP信息 =============")
    ip = get_ip_public()
    ip_info = get_ip_info(ip)
    print(ip_info)


def _test_domain2ip():
    print("============== 测试 域名转IP =============")
    res = domain2ip("www.baidu.com")
    print("www.baidu.com >> ", res)


def _test_is_ip():
    print("============== 测试 输入是否是IP =============")
    res = is_ip("wwww.baidu.com")
    print("www.baidu.com is ip? >> ", res)
    res = is_ip("39.156.66.18")
    print("39.156.66.18 is ip? >> ", res)


if __name__ == "__main__":
    _test_get_ip_info()
    _test_domain2ip()
    _test_is_ip()
