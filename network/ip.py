#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 12/7/19 9:01 AM
# @Author : xuezhi.zhang
# @File : test.py
import urllib.request
# import ipdb


def get_ip_public():
    try:
        r = urllib.request.urlopen('http://api.ip.sb/ip', timeout=5)
        ip = r.read().strip()
        ip = str(ip, encoding='utf8')
    except:
        ip = None
        # logging.error("C")
        # return None
    return ip


def get_ip_info():
    """
        返回公网IP的（国家，省，市，运营商）
        
        接口：
            http://freeapi.ipip.net/223.72.93.23 (使用)
            http://ip.t086.com/?ip=223.72.93.23
            https://github.com/lionsoul2014/ip2region
            http://www.cz88.net/ip/
            https://tool.lu/ip/
            `curl -L tool.lu/ip`
            http://ip.taobao.com/service/getIpInfo.php?ip=223.72.93.23
            API - IP.SB     https://ip.sb/api/
            https://api.ip.sb/geoip
            https://www.xiaoz.me/archives/11359
        
    :return: (country, province, city, ISP)
    """
    ip = get_ip_public()
    if ip is None or len(ip) == 0:
        return None
    else:
        try:
            url = 'http://freeapi.ipip.net/' + ip
            r = urllib.request.urlopen(url=url, timeout=5)
            ip_info = r.read().strip()
            ip_info = str(ip_info, encoding='utf8')
            ip_info = ip_info.replace('[', '')
            ip_info = ip_info.replace(']', '')
            ip_info = ip_info.replace('"', '')
            ip_info_list = ip_info.split(",")
            if len(ip_info_list) == 5:
                res = ip_info_list[0], ip_info_list[1], ip_info_list[
                    2], ip_info_list[4]
            else:
                res = None
        except:
            res = None
        return res


# def get_city_offline(database='ipipfree.ipdb'):
#     ip = get_ip_public()
#     if ip is None or len(ip) == 0:
#         return None
#     else:
#         try:
#             db = ipdb.City(database)
#             city_name = db.find_map(ip, "CN")["city_name"]
#         except:
#             city_name = None
#         return city_name


def get_ip_info_taobo():
    ip = get_ip_public()
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip
    r = urllib.request.urlopen(url=url, timeout=5)
    ip_info = r.read().strip()
    return ip_info
    # print(ip_info)
    # ip_info = str(ip_info, encoding='utf8')
    # ip_info = ip_info.replace('[', '')
    # ip_info = ip_info.replace(']', '')
    # ip_info = ip_info.replace('"', '')
    # ip_info_list = ip_info.split(",")


if __name__ == "__main__":
    ip_info = get_ip_info()
    print(ip_info)
    # ip_info = get_ip_info_taobo()
    # print(ip_info)
