# -*- coding: utf-8 -*-
"""
    util.py
    工具类
"""
import time
import re
import struct
import socket


def split_ips(str):
    """
    分割参数中的ip
    :param str:
    :return:
    """
    if str == '':
        return
    else:
        return str.split('-')


def check_ips_valid(ip):
    """
    校验ip是否合法
    :param ip:
    :return:
    """
    if ip == '':
        return False
    else:
        ips = ip.split('.')
        if len(ips) != 4:
            return False
        else:
            return True


def check_ip_same_segment(ip1, ip2):
    """
    校验两个ip是不是同一个网段
    :param ip1:
    :param ip2:
    :return:
    """
    ips1 = ip1.split('.')
    ips2 = ip2.split('.')
    if ips1[0] != ips2[0] or ips1[1] != ips2[1] or ips1[2] != ips2[2]:
        return False
    else:
        return True


def ip2int(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]


def int2ip(int_ip):
    return socket.inet_ntoa(struct.pack('!I', int_ip))


def parse_ip_range(ips):
    match = re.match(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})-(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", ips)

    if match is None:
        raise Exception('解析ip格式出现异常')

    ip_list = match.groups()
    start_ip_int = ip2int(ip_list[0])
    end_ip_int = ip2int(ip_list[1])
    if start_ip_int > end_ip_int:
        raise Exception("ip的范围异常")

    return start_ip_int, end_ip_int


def save_log_file(filename, text):
    """
    写入文件
    :param filename:
    :param text:
    :return:
    """
    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{str(localtime)} : {text} \n')
