#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 12/6/19 1:57 PM
# @Author : xuezhi.zhang
# @File : qrcode.py
import cv2
import os
import zxing
import numpy as np
from .url import url2dict


def qrcode2url(img):
    """
    将二维码转化成URL
    :param img: ndarray or fname
    :return: 
    """
    flag = False
    if (isinstance(img, str)):
        print('str')
        fname = img
    else:
        try:
            img = np.array(img, dtype=np.uint8)
        except:
            pass
        fname = '/tmp/tmp.jpg'
        cv2.imwrite(fname, img)
        flag = True
    # check if file exist.
    if not os.path.isfile(fname):
        raise Exception("%s is not a file." % img)
    reader = zxing.BarCodeReader()
    barcode = reader.decode(fname)
    url = barcode.parsed
    if flag:
        os.system('rm %s' % fname)
    return url


def qrcode2dict(img):
    url = qrcode2url(img)
    conf = url2dict(url)
    return conf
