#!/bin/env python3
import datetime
from history import createUserHistory
from arrRes import dataRequests
from flask import Flask,request
from flask_json import FlaskJSON, JsonError, json_response, as_json
app=Flask(__name__)
FlaskJSON(app)
url="http://alfariqyraihan.com:8080/"
@app.route("/<int:length>")
def lengthData(length):
    datas=dataRequests("example.csv",length)
    createUserHistory("app.log",url+str(length)).create()
    if length > len(datas.file.values):
        return f"data not found<br>data max : {len(datas.file.values)}"
    else:
        return json_response(length_data=len(datas.file.values),requests_data=length,result=datas.processing())
@app.route("/<string:value>")
def invalid(value):
    createUserHistory("app.log",url+str(value)).create()
    return f"requests invalid"
if __name__=="__main__":
    app.run(host="127.0.0.1")
