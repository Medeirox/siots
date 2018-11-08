from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from . import api_v1
import json
import time

@api_v1.route('/api/v1/log/', defaults={'data': None}, methods=['POST'])
@api_v1.route('/api/v1/log/<data>', methods=['GET'])
def logData(data):
    with open("test.txt","a") as fo:
        if(request.method == 'GET'):
            fo.write('[{ip}] [{hora}]<|>{dado}\r\n'.format(ip=request.remote_addr, hora=time.asctime( time.localtime(time.time()) ), dado=data))
        else:
            dt = "<|>".join(request.data.decode('ascii').splitlines())
            fo.write('[{ip}] [{hora}]<|>{dado}\r\n'.format(ip=request.remote_addr, hora=time.asctime( time.localtime(time.time()) ), dado=dt))
    return 'ok'

@api_v1.route('/api/v1/readlog/', methods=['GET', 'POST'])
def readLogData():
    with open("test.txt","r") as fo:
        lns = fo.readlines()
        header = "<html><h1>Registro de Log em [{}]</h1>".format(time.asctime( time.localtime(time.time()) ))
        output = ""
        for i in range(len(lns)):
            output = lns[i] + '<br>' + output
        output += "</html>"
    return (header+output).replace("<|>","<br>")

@api_v1.route('/api/v1/login/<id>', methods=['GET', 'POST'])
def login(id):
    return 'Welcome {0}!'.format(id)

@api_v1.route('/api/v1/update.json', methods=['GET', 'POST'])
def update_json():
    if(request.method == 'GET'):
        return str(request.args)

    if(request.method == 'POST'):
        json_parsed = request.get_json(True,True)
        return json.dumps(json_parsed)

    # if(request.method == 'GET')
    # return str(request.args)
    if(api_key == 0):
        return 'Nenhuma api_key informada'
    else:
        return 'Database updated by {0}!'.format(api_key)