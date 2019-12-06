#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 12/6/19 1:58 PM
# @Author : xuezhi.zhang
# @File : utils.py
import base64


def base64_decode(base64_encode_str):
    """
    利用 base64.urlsafe_b64decode 对字符串解码
    :param base64_encode_str: 
    :return: 
    """
    if base64_encode_str:
        need_padding = len(base64_encode_str) % 4
        if need_padding != 0:
            missing_padding = 4 - need_padding
            base64_encode_str += '=' * missing_padding
        base64_encode_str = base64.urlsafe_b64decode(base64_encode_str).decode(
            'utf-8')
    if not isinstance(base64_encode_str, str):
        base64_encode_str = str(base64_encode_str, encoding='utf-8')
    return base64_encode_str


def base64_encode(input, padding=False):
    """
    利用 base64.urlsafe_b64decode 对字符串编码
    :param input: base64_encode_str
    :return: 
    """
    assert isinstance(input, str), 'the type of input is not str.'
    if len(input) == 0:
        return ''
    input_encode_utf8 = input.encode('utf-8')
    input_encode_base64 = base64.urlsafe_b64encode(input_encode_utf8)
    if padding:
        need_padding = len(input_encode_base64) % 4
        if need_padding != 0:
            missing_padding = 4 - need_padding
            input_encode_base64 += '=' * missing_padding
    if not isinstance(input_encode_base64, str):
        input_encode_base64 = str(input_encode_base64, encoding='utf-8')
    return input_encode_base64


def dict_type_default():
    '''
    protocol_param <- protoparam
    obfs_param <- obfsparam
    server_port <- port
    :return: 
    '''
    conf = {
        "group": "",
        "method": "",
        "obfs": "",
        "obfs_param": "",
        "password": "",
        "protocol": "",
        "protocol_param": "",
        "remarks": "",
        "server": "",
        "server_port": "",
    }
    return conf


def dict_type_url():
    """
    protocol_param -> protoparam
    obfs_param -> obfsparam
    server_port -> port
    :return: 
    """
    conf = {
        "group": "",
        "method": "",
        "obfs": "",
        "obfsparam": "",
        "password": "",
        "port": "",
        "protocol": "",
        "protoparam": "",
        "remarks": "",
        "server": "",
    }
    return conf


def dict_type_default2url(conf):
    assert isinstance(conf, dict), "input is not dict."
    # obfs_param
    conf['obfsparam'] = conf['obfs_param']
    conf.pop('obfs_param')
    # protocol_param
    conf['protoparam'] = conf['protocol_param']
    conf.pop('protocol_param')
    # server_port
    conf['port'] = conf['server_port']
    conf.pop('server_port')
    return conf


def dict_type_url2default(conf):
    assert isinstance(conf, dict), "input is not dict."
    # obfs_param
    conf['obfs_param'] = conf['obfsparam']
    conf.pop('obfsparam')
    # protocol_param
    conf['protocol_param'] = conf['protoparam']
    conf.pop('protoparam')
    # server_port
    conf['server_port'] = conf['port']
    conf.pop('port')
    return conf
