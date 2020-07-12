# -*- coding: utf-8 -*-
"""
    scan_port.py
    作业1： 编写一个基于多进程/多线程模型的主机扫描器
"""
import argparse
import os
import socket
import threading
import util

lock = threading.Lock()


def deal_ping_scan(ips, log_filename=None):
    """
    进行ping的网段处理
    :param ips:
    :return:
    """
    ip_list = util.split_ips(ips)
    if ip_list is None or len(ip_list) == 0:
        raise Exception('ping的ips数据格式错误')
    for ip in ip_list:
        if not util.check_ips_valid(ip):
            raise Exception('ping的ip格式错误')

    start_ip = ip_list[0]
    end_ip = ip_list[1]

    # 校验两个是否同一个网段
    if not util.check_ip_same_segment(start_ip, end_ip):
        raise Exception('ping的ip要在同一个网段')

    ip_range = util.parse_ip_range(ips)

    for int_ip in range(ip_range[0], ip_range[1] + 1):
        t = threading.Thread(target=scan_ip, args=(util.int2ip(int_ip), log_filename))
        t.start()


def scan_ip(ip, log_file_name=None):
    lock.acquire()
    result = os.popen('ping -c 1 -t 1 %s' % ip).read()
    if 'ttl' in result:
        print(f'{ip}可以ping通')

        if log_file_name is not None and log_file_name != '':
            util.save_log_file(log_file_name, f'{ip}--可以Ping通')
    else:
        print(f'{ip}不可以ping通')
        if log_file_name is not None and log_file_name != '':
            util.save_log_file(log_file_name, f'{ip}--不可以Ping通')

    lock.release()


def deal_tcp_scan(ips, log_filename=None):
    for port in range(1, 65536):
        t = threading.Thread(target=socket_ip_status, args=(ips, port, log_filename))
        t.start()


def socket_ip_status(ip, port, log_filename=None):
    lock.acquire()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.connect((ip, port))
        result = f'{ip} port {port} 连接成功'
        if log_filename is not None and log_filename != '':
            util.save_log_file(log_filename, result)
    except Exception as e:
        result = f'{ip} port {port} 无法连接'
        if log_filename is not None and log_filename != '':
            util.save_log_file(log_filename, result)
    finally:
        server.close()
        lock.release()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--number', dest='Number', type=int, required=True, default='1', help='设置启动的线程数量')
    parser.add_argument('-f', '--function', dest='Function', type=str, required=True, default='',
                        choices=['ping', 'tcp'],
                        help='设置连接方式:[支持ping,tcp]')
    parser.add_argument('-ip', '--ip', dest='Ip', type=str, required=True, default='',
                        help='目标的ip地址,如果是ping的方式,则192.168.0.1-192.168.0.100;如果是tcp方式,则127.0.0.1')
    parser.add_argument('-w', '--write', dest='Write', type=str, default='', help='写入目标文件的名称')

    args = parser.parse_args()

    thread_num = args.Number
    function = args.Function
    ips = args.Ip
    write = args.Write

    if thread_num > 10:
        print('当前最多只支持10个线程并发.....')
        raise Exception('当前最多只支持10个线程并发.....')

    print(f'{"*" * 10}开始进行运行程序{"*" * 10}')
    if function == 'ping':
        deal_ping_scan(ips, thread_num, log_filename=write)
    else:
        deal_tcp_scan(ips, log_filename=write)
