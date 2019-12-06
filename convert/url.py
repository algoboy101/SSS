#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 12/6/19 1:57 PM
# @Author : xuezhi.zhang
# @File : url.py
import qrcode
from .utils import dict_type_url, base64_decode


def url2qrcode(url=None):
    """
    将URL转化成二维码
    :param url: 
    :return: 
    """
    '''
    所谓高级用法，就是设置二维码大小、颜色等参数的写法。示例代码如下，其中实例化参意义如下：
        version参数----二维码的格子矩阵大小，可以是1到40，1最小为21*21，40是177*177
        error_correction参数----二维码错误容许率，默认ERROR_CORRECT_M，容许小于15%的错误率
        box_size参数----二维码每个小格子包含的像素数量
        border参数----二维码到图片边框的小格子数，默认值为4
    '''
    if url is None:
        return None
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data=url)
    # setup color
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # img.show() # show code
    return img


def url2dict_ss(url):
    """
    格式： method:password@server:server_port -> base64 -> ss://base64
    :param url: 
    :return: 
    """
    url = url[5:]
    conf = dict_type_url()
    decode_str = base64_decode(url)
    parts = decode_str.split(':')
    if len(parts) != 3:
        print('不能解析SS链接: %s' % url)
        return
    conf['method'] = parts[0]
    conf['password'] = parts[1].split("@")[0]
    conf['server'] = parts[1].split("@")[1]
    conf['server_port'] = parts[2]
    return conf


def url2dict_ssr(url):
    """
    解析SSR链接到dict
    格式说明：
        server:server_port:protocol:method:obfs:password_params
        password/?others
        key1=v1&key2=v2...
    :param url: SSR 链接
    :return: SSR链接解析结果
    """
    url = url[6:]
    conf = dict_type_url()
    decode_str = base64_decode(url)
    parts = decode_str.split(':')
    if len(parts) != 6:
        print('不能解析SSR链接: %s' % url)
        return
    conf['server'] = parts[0]
    conf['server_port'] = parts[1]
    conf['protocol'] = parts[2]
    conf['method'] = parts[3]
    conf['obfs'] = parts[4]
    password_and_params = parts[5]
    password_and_params = password_and_params.split("/?")
    conf['password'] = base64_decode(password_and_params[0])
    if len(password_and_params) > 1 and password_and_params[1]:
        param_dic = {}
        param_parts = password_and_params[1].split('&')
        for part in param_parts:
            key_and_value = part.split('=')
            param_dic[key_and_value[0]] = key_and_value[1]
        conf['obfsparam'] = base64_decode(param_dic.get('obfsparam', ""))
        conf['protoparam'] = base64_decode(param_dic.get('protoparam', ""))
        conf['remarks'] = base64_decode(param_dic.get('remarks', ""))
        conf['group'] = base64_decode(param_dic.get('group', ""))
    return conf


def url2dict(url):
    """
    :param url: 
    :return: 
    """
    url_parts = url.split(':')
    if url_parts[0] == 'ss':
        res = url2dict_ss(url)
    elif url_parts[0] == 'ssr':
        res = url2dict_ssr(url)
    else:
        raise Exception("Just support SS or SSR. Not Suport type: %s <- %s" %
                        (url_parts[0], url))
    return res
