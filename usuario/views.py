from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from .models import *
from auto import utils

# Create your views here.
def getUsuario(request, id):

	if request.method == 'GET':
		res = []
		usuario= Usuario.objects.filter()
		for usua in usuario:
			diccionario={"id":usua.id,"nombre":usua.nombre,"apellido":usua.apellido,
            "correo":usua.correo,"contrasena":usua.contrasena}
			if  id==usua.id :
				return JsonResponse(diccionario,safe=False)
			res.append(diccionario)
		return JsonResponse(res,safe=False)
		
	elif (request.method == 'POST'):
		body = utils.request_todict(request)
		nombre = body.get("nombre", None)
		apellido = body.get("apellido", None)
		correo = body.get("correo", None)
		contrasena = body.get("contrasena", None)
		try:
			usuario = Usuario().crearUsuario(nombre, apellido, correo, contrasena)
			return JsonResponse({
                'STATUS' : 'OK',
                'CODIGO' : 200,
                'DETALLE' :  utils.response_message("Usuario","creado",usuario.to_string())
            })
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method,"usuario",e)
            })

	elif (request.method == 'PUT'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		nombre = body.get("nombre", None)
		apellido = body.get("apellido", None)
		correo = body.get("correo", None)
		contrasena = body.get("contrasena", None)
		try:
			usuario = Usuario().actualizarUsuario(id,nombre, apellido, correo, contrasena)
			if usuario:
				return JsonResponse({
                	'STATUS' : 'OK',
                	'CODIGO' : 200,
                	'DETALLE' :  utils.response_message("Usuario","actualizado",usuario.to_string())
            	})
			else:
				return JsonResponse({
                	'STATUS' : 'Error',
                	'CODIGO' : 404,
                	'DETALLE' :  utils.error_message_1("Usuario",id)
            	})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "usuario",e)
            })
	
	elif(request.method == 'DELETE'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		try:
			mensaje = Usuario().eliminarUsuario(id)
			if(mensaje != ""):
				return JsonResponse({
                	'STATUS' : 'OK',
                	'CODIGO' : 200,
                	'DETALLE' :  mensaje
           		})
			else:
				return JsonResponse({
                	'STATUS' : 'Error',
                	'CODIGO' : 404,
                	'DETALLE' : utils.error_message_1("Usuario",id)
           		})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "usuario",e)
            })

	else:
		return HttpResponse(status=404)

def getOneUsuario2(request,pk):
	if request.method == 'GET':
		diccionario = {}
		usuario = Usuario.objects.get(pk=pk)
		if usuario:
			diccionario = {"autor" : usuario.nombre + " " + usuario.apellido}
		return JsonResponse(diccionario,safe=False)
	else:
		return HttpResponse(status=404)

def getAllUsers(request):
	if request.method == 'GET':
		res = []
		usuario= Usuario.objects.filter()
		for usua in usuario:
			diccionario={"id":usua.id,"nombre":usua.nombre,"apellido":usua.apellido,
            "correo":usua.correo,"contrasena":usua.contrasena}
			res.append(diccionario)
		return JsonResponse(res,safe=False)
	else:
		return HttpResponse(status=404)


