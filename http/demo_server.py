# _*_ coding: UTF-8 _*_
# @Time     : 2020/10/12 13:22
# @File     : demo_server.py

from flask import Flask, session, request, Request, make_response

app = Flask(__name__)
request: Request
app.secret_key = "key"


def hello():
    query = request.args
    post = request.form
    return f"query:{query}\n" \
           f"post:{post}"
