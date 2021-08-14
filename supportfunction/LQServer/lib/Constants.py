"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software:
@file: Constants.py
@time: 2021/08/08 16:52
"""
import os

import yaml


class Constants:

    def __init__(self):
        self.ROOT_PATH = os.path.join(os.getcwd().split('lib')[0], 'config')

    def conf_data_filter(self, env, sys_name) -> dict:
        """
            获取连接数据
            :param path:  文件路径
            :param sys_name: 系统名称
            :return: dict
        """

        self.ENV_PATH = os.path.join(self.ROOT_PATH, f"{env}.yml")
        with open(self.ENV_PATH, encoding='utf-8') as conf:
            _dict = yaml.safe_load(conf)

        return _dict.get(sys_name)


