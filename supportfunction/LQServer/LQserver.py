"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software:
@file: LQserver.py
@time: 2021/08/08 18:52
"""

from flask import Flask
from flask_cors import CORS
from lib.GetLog import GetLog

app = Flask(__name__)
# 解决跨域问题
CORS(app, supports_credentials=True)

@app.route('/')
def lqserver():

    return

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)



