"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software:
@file: GetLog.py
@time: 2021/08/08 17:52
"""

# 用于ssh连接的python库
import paramiko
import logging
from .Constants import Constants


class GetLog(Constants):
    """获取后台日志"""

    def __init__(self):
        super().__init__()
        # 设置连接开关
        self.trans = None
        # 设置环境变量
        self.env = None

    def __get_command(self, log_path, key, rows: list):
        """
            获取读取日志的sh指令
            :param log_path: 日志绝对路径
            :param key:  搜索键值
            :param rows: 搜索行号,接收list/tuple
            :return: tuple
        """
        # 键值前n行
        key_before = f"cat -n {log_path} |grep '{key}' -B {rows[0]}"
        # 键值前n行
        key_behind = f"cat -n {log_path} |grep '{key}' -A {rows[1]}"

        return key_before, key_behind

    def __connect_logsystem(self, hostname, connect_data, order):
        """
            连接日志系统，返回ssh对象
            :param hostname: 日志主机IP
            :param connect_data: 连接数据
            :param order: 指令
            :return:
        """
        # 建立一个transport对象
        self.trans = paramiko.Transport(hostname, connect_data['port'])
        # 建立连接
        self.trans.connect(username=connect_data["username"],
                           password=connect_data["password"])
        #  建立sshclient对象
        ssh = paramiko.SSHClient()
        ssh._transport = self.trans
        # 发送指令，60s连接不上报超时
        rltin, rltout, rlterr = ssh.exec_command(command=order, timeout=60)
        logging.info("日志系统连接成功，且已执行相关指令")

        return rltout

    def __read_log(self, key, sys_name):
        """
            将满足条件的日志输出
            :param key: 关键词
            :param sys_name: 系统名称
            :return:
        """

        temp_list, appear_No = [], []
        # 连接数据
        connect_data = self.conf_data_filter(self.env, sys_name)
        if not connect_data:
            logging.error("无对应的系统配置信息，请添加")
            return {}
        # 获取指令
        orders = self.__get_command(connect_data['LogPath'], key, [8, 300])
        for url in connect_data['url']:
            # 获取日志对象
            stdout0 = self.__connect_logsystem(url, connect_data, orders[0])
            stdout1 = self.__connect_logsystem(url, connect_data, orders[1])
            # 对对象进行转码
            temp_str0 = stdout0.read().decode()
            temp_str1 = stdout1.read().decode()
            # 得到总的日志字符
            temp_str = temp_str0 + temp_str1
            # 若多个系统出现同一key值，保存出现的次数
            appear_No.append(temp_str.count(key))
            # 同时将日志也添加到列表中
            temp_list.append(temp_str)

        logging.info("获取日志成功")
        # 获取键值出现次数最多的那个系统的日志
        log = temp_list.pop(appear_No.index(max(appear_No)))
        # 关闭连接
        self.trans.close()

        return log

    def get_log(self, key, sys_name, env='uat'):
        """
            获取日志
            :param key:
            :param sys_name:
            :param stage:
            :return:
        """

        self.env = env

        if not key or not sys_name:
            return {
                "result": {
                    "log": "",
                    "err_code": 404,
                    "message": "没有输入键值/系统名称"
                },
                "code": 200
            }

        log = self.__read_log(key, sys_name)
        if not log:
            return {
                "result": {
                    "log": "",
                    "err_code": 401,
                    "message": "没有找到对应的日志信息"
                },
                "code": 200
            }

        else:
            return {
                "result": {
                    "log": log,
                    "err_code": 200,
                    "message": "获取成功"
                },
                "code": 200
            }


if __name__ == '__main__':
    key = "qazWERT1234566678"
    print(GetLog().get_log(key, 'a', 'st'))


