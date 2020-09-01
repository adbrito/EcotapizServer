import json
import math

def request_todict(request):
    try:
        body = request.body.decode('utf-8')
        body = json.loads(body)
        return body
    except:
        return {}

def response_message(string1, string2,object):
    return 'El objeto ' + str(string1) + ' ' + str(string2) +'tiene los siguientes atributos: ' + str(object)

def error_message_1(string1, id):
    return str(string1) + " con id " + str(id) + " no se encuentra en la base de datos"

def message_1(string1, id):
    return str(string1) + " con id " + str(id) + " eliminado exitosamente de la base de datos"   

def error_message_2(method,string1, e):
    return 'Error en ' + str(method) + " en la tabla "+ str(string1) + " - mensaje: " + str(e) 