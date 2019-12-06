#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 12/6/19 2:16 PM
# @Author : xuezhi.zhang
# @File : test_convert.py
import sys
sys.path.append('.')
sys.path.append('..')
from convert.url import url2dict
from convert.dict import dict2url_ss, dict2url_ssr, dict2qrcode
from convert.qrcode import qrcode2dict
import pprint


def isequal_dict(dict1, dict2):
    for key in dict1.keys():
        if key not in dict2.keys():
            return False
        if dict1[key] != dict2[key]:
            return False
    return True


url_list = [
    "ssr://MTQyLjkzLjg0LjE1Mzo4ODgwOmF1dGhfY2hhaW5fYTpub25lOnBsYWluOmJYbGFha0kxYWtoMVpuaFZNRGhLWWxkd1lYTnpkMjl5WkE",
    "ssr://NTAuMy4yNDIuMTMzOjEyNTE0OmF1dGhfc2hhMV92NDpjaGFjaGEyMDpodHRwX3NpbXBsZTpOalUwTnprLz9vYmZzcGFyYW09JnByb3RvcGFyYW09JnJlbWFya3M9Nzd5SU1URXVNVEh2dklubGhZM290TG5tdFl2b3I1WG9pb0xuZ3JrSzZabVE2WUNmTXpBd2EySXZjLW1jZ09pbWdlbXJtT21Bbi1lYWhPaUtndWVDdVZGUk1USXdPREU0TmpreU53Jmdyb3VwPQ",
    "ssr://OTEuMTkyLjgxLjMxOjgwOmF1dGhfY2hhaW5fYTpub25lOmh0dHBfc2ltcGxlOllXUnRhVzVoWkcxcGJtRmtiV2x1Lz9vYmZzcGFyYW09JnByb3RvcGFyYW09TVRweGNYRjNaR1kmcmVtYXJrcz01TC1FNVp1OSZncm91cD0",
    "ssr://MTY3LjE3OS43NC4zNDoyNzcwMTphdXRoX2NoYWluX2E6bm9uZTpwbGFpbjpPRGs0TkRJNGFHaGtjZy8_b2Jmc3BhcmFtPSZwcm90b3BhcmFtPSZyZW1hcmtzPTZMU3Q1TG13NVlxZ1VWRTFNVFl3TkRVNEN1LThpT2F0cE9XSWh1UzZxLW1aa09tQW4tLThpUSZncm91cD0",
    "ssr://MTc2LjMyLjM1LjI1NDoyNTAzMTphdXRoX2NoYWluX2E6YWVzLTI1Ni1jZmI6cGxhaW46TmpVME16SXgvP29iZnNwYXJhbT0mcHJvdG9wYXJhbT0mcmVtYXJrcz1NVGMyTGpNeUxqTTFMakkxTkEmZ3JvdXA9",
    "ssr://MTM5LjE4MC4yMTMuMjE6MTY0Mjc6b3JpZ2luOmFlcy0yNTYtY2ZiOnBsYWluOk1XTlZSR1kxLz9vYmZzcGFyYW09JnByb3RvcGFyYW09JnJlbWFya3M9YUhWcExXcHBMbmg1ZXVhenFPV0dqT21BZ1RFd1ItYTFnZW1Iai1hV3NPV0tvT1dkb1EmZ3JvdXA9NTRHdzVweTY",
    "ssr://MTc2LjMyLjM1LjI1NDoyNTAzMTpvcmlnaW46YWVzLTI1Ni1jZmI6cGxhaW46TmpVME16SXg",
    "ss://YWVzLTI1Ni1jZmI6c3N4LnJlLTA1MTUyNDI2QDIwNi4xODkuMTUxLjU5OjEyMDAy",
    "ssr://MTI3LjAuMC4xOjEyMzQ6YXV0aF9hZXMxMjhfbWQ1OmFlcy0xMjgtY2ZiOnRsczEuMl90aWNrZXRfYXV0aDpZV0ZoWW1KaS8_b2Jmc3BhcmFtPVluSmxZV3QzWVRFeExtMXZaUSZyZW1hcmtzPTVyV0w2Sy1WNUxpdDVwYUg",
    "ssr://MTI3LjAuMC4xOjEyMzQ6YXV0aF9hZXMxMjhfbWQ1OmFlcy0xMjgtY2ZiOnRsczEuMl90aWNrZXRfYXV0aDpZV0ZoWW1KaS8_b2Jmc3BhcmFtPVluSmxZV3QzWVRFeExtMXZaUQ"
]


def test_url_dict():
    """
    URL -> conf
    conf -> URL2
    URL2 -> conf2
    check conf == conf2
    :return: 
    """
    for url in url_list:
        conf = url2dict(url)
        img = dict2qrcode(conf)
        conf2 = qrcode2dict(img)
        flag = isequal_dict(conf, conf2)
        print(flag)


def test_dict_qrcode():
    """
    URL -> conf
    conf -> url -> qrcode
    qrcode ->  url -> conf2
    check conf == conf2
    :return: 
    """
    for url in url_list:
        conf = url2dict(url)
        if url[:3] == 'ssr':
            url2 = dict2url_ssr(conf)
        else:
            url2 = dict2url_ss(conf)
        # print(url)
        # print(url2)
        conf2 = url2dict(url2)
        # pprint.pprint(conf)
        # pprint.pprint(conf2)
        flag = isequal_dict(conf, conf2)
        print(flag)


if '__main__' == __name__:
    test_url_dict()
