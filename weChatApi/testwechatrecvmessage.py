# -*- coding: utf-8 -*-
from flask import Flask, request, json
import requests
import urllib

app = Flask(__name__)

@app.route('/')
def hello():
    return 'OK'

# 接收消息
@app.route('/recvmessage', methods=['POST'])
def test():
    data = request.form.get('wsg')
    print(request.form.get('wxid'))
    print(request.form.get('wxgh'))
    print(data)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)