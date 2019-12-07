#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 12/7/19 4:45 PM
# @Author : xuezhi.zhang
# @File : speed.py
import os
import sys
sys.path.append('.')
from .ip import is_ip
import time
import urllib.request
import logging
import socket
import socks
default_socket = socket.socket
import subprocess
import signal
'''
    used to test latency
    使用固定顺序的5个链接，比随机的访问，结果更加公平；
    使用一个链接，访问次数太多，可能被封掉。
'''
_url_list = [
    'https://twitter.com/',
    'https://www.facebook.com/',
    'http://gmail.com/',
    'https://scholar.google.co.jp/scholar?q=Deep+object+tracking+with+multi-modal+data',
    'https://www.google.com/search?q=blog.xuezhisd.top',
]


def get_ping_time(server="www.baidu.com", count=1, wait_time=2):
    """
    测试ping的时间
    :param server: ip or domain name
    :param count: 次数
    :param w: 等待时间
    :return: 
    """
    ping_len = "7" if is_ip(server) else "8"
    cmd = "ping -c %s -w %s %s |grep 'time=' | awk '{print $%s}' |cut -b 6-" % (
        count, wait_time, server, ping_len)
    ping_res = os.popen(cmd).readlines()
    try:
        cmd = "ping -c %s -w %s %s |grep 'time=' | awk '{print $%s}' |cut -b 6-" % (
            count, wait_time, server, 8)
        ping_res = os.popen(cmd).readlines()
        ping_res = [int(float(item.strip())) for item in ping_res]
    except:
        cmd = "ping -c %s -w %s %s |grep 'time=' | awk '{print $%s}' |cut -b 6-" % (
            count, wait_time, server, 7)
        ping_res = os.popen(cmd).readlines()
        ping_res = [int(float(item.strip())) for item in ping_res]
        # return False, None
    if len(ping_res) == 0:
        ping_time = None
        status = False
    else:
        try:
            ping_time = sum(ping_res) / float(len(ping_res))
            status = True
        except:
            logging.warning("divide zero?")
            ping_time = None
            status = False
    return status, ping_time


def get_port_connect(ip, port):
    port = port if isinstance(port, int) else int(port)
    print('\033[1m*Port\033[0m %s:%d' % (ip, port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        print('\033[1;32m.... is OK.\033[0m')
        return True
    except socket.timeout:
        print('\033[1;33m.... is down or network time out!!!\033[0m')
        return False
    except:
        print('\033[1;31m.... is down!!!\033[0m')
        return False


def get_latency_url(url, proxy_ip='127.0.0.1', proxy_port='1080', timeout=5):
    """
    访问一个网页，统计延迟
    :param url: 
    :param timeout: 
    :return: 
    """

    # 设置代理
    def create_connection(address, timeout=timeout, source_address=None):
        sock = socks.socksocket()
        sock.settimeout(timeout=timeout)
        sock.connect(address)
        return sock

    socks.set_default_proxy(proxy_type=socks.PROXY_TYPE_SOCKS5,
                            addr=proxy_ip,
                            port=proxy_port)
    socket.socket = socks.socksocket
    socket.create_connection = create_connection

    status = True
    start = time.time()
    try:
        r = urllib.request.urlopen(url, timeout=timeout)
        r.read()
    except:
        logging.warning("can't visit url: %s" % url)
        status = False
        return status, timeout
    end = time.time()
    latency = end - start
    return status, latency


# 获取平均延迟 一般>=5s就可以认为这个代理无效
def get_latency_average(count=1,
                        proxy_ip='127.0.0.1',
                        proxy_port='1080',
                        timeout=5):
    """
    访问多个网页，统计平均延迟
    :param count: 访问网页的个数，最大为5
    :return: 
    """
    # 边界检查
    if count < 1:
        count = 1
    elif count >= len(_url_list):
        count = len(_url_list)
    # 多次访问，统计平均值
    time_sum = 0
    t = 0
    for ind in range(count):
        cur_status, cur_time = get_latency_url(_url_list[ind],
                                               proxy_ip=proxy_ip,
                                               proxy_port=proxy_port,
                                               timeout=timeout)
        if cur_status:
            time_sum += cur_time
            t += 1
        else:
            continue
    if t > 0:
        status = True
        time_mean = time_sum / float(t)
    else:
        status = False
        time_mean = 9999
    return status, time_mean


def get_ssr_ping_latency(ssr,
                         exes="shadowsocksr/shadowsocks/local.py",
                         local_ip='127.0.0.1',
                         local_port=39613,
                         timeout=20):
    # 找出残留进程
    pids = os.popen(
        'ps -ef | grep "shadowsocks/local.py" | grep -v "grep" | awk \'{print $2}\''
    ).read()
    pid_list = pids.strip().split("\n")
    logging.info("old process： %s" % str(pid_list))
    # 杀死残留进程
    for pid in pid_list:
        if pid:
            pid = int(pid)
            os.kill(pid, signal.SIGKILL)
    logging.info("killed old process.")
    # 根据阐述，开启新的进程
    cmd = "python %s -qq -s %s -p %s -k %s -m %s -O %s -o %s -b %s -l %s " % (
        exes, ssr['server'], ssr['port'], ssr['password'], ssr['method'],
        ssr['protocol'], ssr['obfs'], local_ip, local_port)
    if len(ssr.get('protoparam', "")) > 1:
        cmd += "-G %s " % ssr['protoparam']
    if len(ssr.get('obfsparam', "")) > 1:
        cmd += "-g %s " % ssr['obfsparam']
    proc = subprocess.Popen(cmd, shell=True)
    logging.info("start new process.")

    # test ping
    server_name = ssr['server']
    ping_status, ping_time = get_ping_time(server_name, count=1, wait_time=2)
    logging.info("end ping test.")

    # test latency
    if ping_status:
        latency_status, latency_time = get_latency_average(
            count=1, proxy_ip=local_ip, proxy_port=local_port, timeout=timeout)
    else:
        latency_status = False
        latency_time = 9999
    logging.info("end latency test.")

    return ping_status, ping_time, latency_status, latency_time
