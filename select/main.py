#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 12/7/19 9:08 PM
# @Author : xuezhi.zhang
# @File : main.py

import sys
sys.path.append('.')
sys.path.append('..')
from convert.url import url2dict
from network.speed import get_ssr_ping_latency
if __name__ == "__main__":
    print(len(sys.argv))
    assert len(sys.argv) > 1, "Usage: python3 main.py input.txt"
    fname_in = sys.argv[1]
    len_params = len(sys.argv)
    if len_params < 4:
        fname_out_bad = "select_bad.txt"
    else:
        fname_out_bad = sys.argv[3]

    if len_params < 3:
        fname_out_good = "select_good.txt"
    else:
        fname_out_good = sys.argv[2]

    with open(fname_in, "r") as fp:
        ssr_list = fp.readlines()
    ssr_list = [ssr.strip() for ssr in ssr_list]
    for ssr_url in ssr_list:
        ssr_dict = url2dict(ssr_url)

        ping_status, ping_time, latency_status, latency_time = get_ssr_ping_latency(
            ssr_dict,
            exes="../shadowsocksr/shadowsocks/local.py",
            local_ip='127.0.0.1',
            local_port=39613,
            timeout=20)
        if ping_status and latency_status:
            print(ssr_dict)
            with open(fname_out_good, "a+") as fp:
                fp.write(ssr_url + "\n")
        else:
            with open(fname_out_bad, "a+") as fp:
                fp.write(ssr_url + "\n")
        # print(ssr_dict)
