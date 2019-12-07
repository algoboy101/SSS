#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 12/6/19 2:16 PM
# @Author : xuezhi.zhang
# @File : test_convert.py
import sys
sys.path.append('.')
sys.path.append('..')
from convert.utils import base64_decode
import urllib.request

url = 'https://muma16fx.netlify.com/'

ssr_subscribe = urllib.request.urlopen(url).read().decode(
    'utf-8')  #获取ssr订阅链接中数据
ssr_subscribe_decode = base64_decode(ssr_subscribe)
ssr_subscribe_decode = ssr_subscribe_decode.replace('\r', '')
print(ssr_subscribe_decode)
