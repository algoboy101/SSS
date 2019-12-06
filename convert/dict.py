#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 12/6/19 1:57 PM
# @Author : xuezhi.zhang
# @File : dict.py

from .utils import base64_encode
from .url import url2qrcode


def dict2url_ss(conf):
    """
    将配置转成SS链接
    :param conf: 
    :return: 
    """
    passwd_server = "@".join([conf['password'], conf['server']])
    parts = ":".join([conf['method'], passwd_server, conf['server_port']])
    parts_encode = base64_encode(parts)
    res = "ss://" + parts_encode
    return res


def dict2url_ssr(conf):
    """
    将配置转成SSR链接
    :param conf: 
    :return: 
    """
    others = []
    # part 1
    if 'obfsparam' in conf:
        v_obfsparam = base64_encode(conf['obfsparam'])
        others.append('='.join(['obfsparam', v_obfsparam]))
    elif 'obfs_param' in conf:
        v_obfsparam = base64_encode(conf['obfs_param'])
        others.append('='.join(['obfsparam', v_obfsparam]))
    if 'protoparam' in conf:
        v_protoparam = base64_encode(conf['protoparam'])
        others.append('='.join(['protoparam', v_protoparam]))
    elif 'protocol_param' in conf:
        v_protoparam = base64_encode(conf['protocol_param'])
        others.append('='.join(['protoparam', v_protoparam]))
    if 'remarks' in conf:
        v_remarks = base64_encode(conf['remarks'])
        others.append('='.join(['remarks', v_remarks]))
    if 'group' in conf:
        v_group = base64_encode(conf['group'])
        others.append('='.join(['group', v_group]))
    others_str = '&'.join(others)
    # part 2
    password_str = base64_encode(conf['password'])
    password_others_str = '/?'.join([password_str, others_str])
    # part 3
    all_list = list()
    all_list.append(conf['server'])
    all_list.append(conf['server_port'])
    all_list.append(conf['protocol'])
    all_list.append(conf['method'])
    all_list.append(conf['obfs'])
    all_list.append(password_others_str)
    all_str = ':'.join(all_list)
    all_encode = base64_encode(all_str)
    # part 4
    res = "ssr://" + all_encode
    return res


def dict2qrcode(conf):
    url = dict2url_ssr(conf)
    img = url2qrcode(url)
    return img
