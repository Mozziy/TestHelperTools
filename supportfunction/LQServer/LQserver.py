"""
@author: Albertz
@license: (C) Copyright 2020-2099, Node Supply Chain Manager Corporation Limited.
@contact: 1290136870@qq.com
@software:
@file: LQserver.py
@time: 2021/08/08 18:52
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from lib.GetLog import GetLog

app = Flask(__name__)
# 解决跨域问题
CORS(app, supports_credentials=True)

@app.route('/', methods=['post'])
def lqserver():
    req_data = request.json.get('_value')
    # log = GetLog().get_log(req_data['keyword'], req_data['sysValue'], req_data['envValue'])
    # print(log)
    return jsonify(GetLog().get_log(req_data['keyword'], req_data['sysValue'], req_data['envValue']))

if __name__ == '__main__':
    app.run(host='192.168.8.111', port=9000, debug=True)



