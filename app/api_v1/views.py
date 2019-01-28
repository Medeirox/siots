from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from . import api_v1
from .models import Feed, Device
import traceback
import json
import time
import random, string

#REMOVER
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

#REMOVER
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

#REMOVER
@api_v1.route('/api/v1/login', methods=['GET', 'POST'])
def login():
    if(request.args['pass']=='pass'):
        return 'Welcome {0}!'.format(request.args['user'])
    else:
        return 'login error'


# @api_v1.route('/api/v1/update/<id>/<op>/', methods=['GET', 'POST'])
# def test_call(id,op):
#     return 'ID: {0} | Operation: {1}'.format(id, op)


@api_v1.route('/api/v1/<device_id>/register_device.json', methods=['GET', 'POST'])
def register_device(device_id):

    exists = False
    creation_ok = False
    json_parsed = ''

    if(request.method == 'GET'):
        json_parsed = request.args
    
    if(request.method == 'POST'):
        json_parsed = request.get_json(True,True)

    try:
        dev = Device.get(str(device_id))
        exists = True
    except:
        exists = False
    try:
        if(not exists):
            #Generate write key
            generated_write_key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
            #Generate activation key
            generated_activation_key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

            admin_device = Device.get('admin_device')
            if(admin_device.write_key == json_parsed['write_key']):
                new_device = Device(id=device_id, 
                                    device_type=json_parsed['device_type'],
                                    write_key=generated_write_key, 
                                    activation_key=generated_activation_key,
                                    tag=json_parsed['device_type'], 
                                    created_at=round(time.time(),3),
                                    last_seen=round(time.time(),3), 
                                    status='created',
                                    enabled=0, 
                                    config=json_parsed['config'] if 'config' in json_parsed else None)
                new_device.save()
                print('Just created a new device: {0}'.format(new_device))
                creation_ok = True
    except Exception as e:
        print('Error during the creation of the Device {0}.\nError: {1}'.format(device_id, e))

    if(exists or (not creation_ok) ):
        return ('400')
    else:
        return ('200')


#TODO FALTA VERIFICAR SE O WRITE_KEY CONFERE COM A TABELA DE DEVICES
# Persiste o dado de um unico dispositivo na base de dados
@api_v1.route('/api/v1/<device_id>/update.json', methods=['GET', 'POST'])
def update_json(device_id):

    try:
        data=''
        errorCode=0
        errorCodeDescription=''
        json_parsed=''

        if(request.method == 'POST'):
            json_parsed = request.get_json(True,True)
            print('device_id' in json_parsed)

        #Tratamento do request GET
        #Verificaçao do padrao do pacote
        if(request.method == 'GET'):
            print(type(json_parsed))
            json_parsed = request.args
            print(type(request.args))
        package_ok = ('device_id' in json_parsed) and \
                    ('timestamp' in json_parsed) and \
                    ('data' in json_parsed) and \
                    ('write_key' in json_parsed)
        if(json_parsed['data'] is None):
            pass
        else:
            data=json.dumps(json.loads(json_parsed['data']))
            if(data is None):
                package_ok = False

        if(not package_ok):
            print('Received data format is incorrect')
            errorCode=1 #Received data format is incorrect
            errorCodeDescription='Received data format is incorrect'
        else:
            #Verifica se o equipamento está cadastrado e se a chave confere
            try:
                dev = Device.get(json_parsed['device_id'])
                package_ok = True if dev.write_key == json_parsed['write_key'] else False
                if(not package_ok):
                    print('Informed write_key differs from the database')
                    errorCode=2
                    errorCodeDescription='Informed write_key differs from the database'

            except Exception as ex:
                print('There was a problem while looking for the Device_ID {0} \
                    in the database\nError:{1}'.format(json_parsed['device_id'], ex))
                package_ok = False
                errorCode=3
                errorCodeDescription='There was a problem while looking for the Device_ID {0} \
                    in the database'.format(json_parsed['device_id'])

        if package_ok:
            f = Feed(device_id=json_parsed['device_id'], 
                    timestamp=round(float(json_parsed['timestamp']),3),
                    created_at=round(time.time(),3),
                    data=data)
            check_feed=''
            try:
                # print('check_feed: {}'.format(check_feed))
                check_feed = Feed.get(f.device_id, f.timestamp)
                # print('check_feed: {}'.format(check_feed))
            except Exception as j:
                # print(j)
                print(f)
                f.save()
                print('Feed successfully persisted\n{0}'.format(f._get_json()))
                return str('200')
            #if(check_feed != '')
                # if(check_feed.device_id == f.device_id and check_feed.timestamp == f.timestamp):
                #     print('Identical feed found on the database! Feed will be rejected.')
                # else:
                #     print(f)
                #     f.save()
                #     print('Feed successfully persisted')
                #     return str('200')
            
            return str('400')
    except Exception as e:
        print('An error ocurred during the reception of the feed: \n{0}\n{1}\n{2}'.format(json_parsed,e,traceback.print_exc()))
        return str('400')

    #Tratamento do request POST
    #Verificaçao do padrao do pacote
    if(request.method == 'POST'):
        json_parsed = request.get_json(True,True)
        package_ok = False
        if(not (json_parsed is None) ):
            package_ok = ('device_id' in json_parsed) and \
                     ('timestamp' in json_parsed) and \
                     ('data' in json_parsed) and \
                     ('write_key' in json_parsed)
        if package_ok:
            return str('200')
        else:
            return str('400')
        return json.dumps(json_parsed)

    # if(request.method == 'GET')
    # return str(request.args)
    # if(api_key == 0):
    #     return 'Nenhuma api_key informada'
    else:
        return str('400')
        # return 'Database updated by {0}!'.format(api_key)