#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 12/7/19 9:01 AM
# @Author : xuezhi.zhang
# @File : test.py
import urllib.request
# import ipdb
import re
import os


def is_ip(server="127.0.0.1"):
    pattern = re.compile(
        '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if pattern.match(server):
        return True
    else:
        return False


# def domain2ip(server="www.baidu.com"):
#     ip = os.popen("ping -c 1 %s |grep 'time=' | awk '{print $4}' |cut -b 1-" %
#                   server).readline().strip()
#     # 被墙的域名，无法获取它的IP地址
#     if not ip:
#         ip = None
#     return ip
def domain2ip(server="www.baidu.com", port='http'):
    import socket
    try:
        myaddr = socket.getaddrinfo(server, 'http')
        ip = myaddr[0][4][0]
    except:
        ip = None
    return ip


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


def get_ip_info(ip="127.0.0.1"):
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
    # ip = get_ip_public()
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

    # ip_info = get_ip_info_taobo()
    # print(ip_info)
