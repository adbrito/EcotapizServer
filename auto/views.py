from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from auto import utils 
from .models import *
import json

# Create your views here
def getAuto(request):
	if (request.method == 'GET'):
		res = []
		auto= Auto.objects.all()
		for aut in auto:
			#print(aut)
		
			diccionario={"id":aut.id,"nombre":aut.nombre,"descripcion":aut.descripcion,
            "glb":aut.glb, "imagen":aut.imagen, "ranking":aut.ranking}
			res.append(diccionario)
		return JsonResponse(res,safe=False)

	elif (request.method == 'POST'):
		body = utils.request_todict(request)
		nombre = body.get("nombre", None)
		descripcion = body.get("descripcion", None)
		glb = body.get("glb", None)
		imagen = body.get("imagen", None)
		ranking = body.get("ranking", None)
		try:
			nuevo_auto = Auto().crearAuto(nombre, descripcion, glb, imagen, ranking)
			return JsonResponse({
                'STATUS' : 'OK',
                'CODIGO' : 200,
                'DETALLE' :  utils.response_message("Auto","creado",nuevo_auto.to_string())
            })
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method,"auto",e)
            })

	elif (request.method == 'PUT'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		nombre = body.get("nombre", None)
		descripcion = body.get("descripcion", None)
		glb = body.get("glb", None)
		imagen = body.get("imagen", None)
		ranking = body.get("ranking", None)
		try:
			nuevo_auto = Auto().actualizarAuto(id,nombre, descripcion, glb, imagen, ranking)
			if nuevo_auto:
				return JsonResponse({
                	'STATUS' : 'OK',
                	'CODIGO' : 200,
                	'DETALLE' :  utils.response_message("Auto","actualizado",nuevo_auto.to_string())
            	})
			else:
				return JsonResponse({
                	'STATUS' : 'Error',
                	'CODIGO' : 404,
                	'DETALLE' :  utils.error_message_1("Auto",id)
            	})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "auto",e)
            })
	
	elif(request.method == 'DELETE'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		try:
			mensaje = Auto().eliminarAuto(id)
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
                	'DETALLE' : utils.error_message_1("Auto",id)
           		})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "auto",e)
            })

	else:
		return HttpResponse(status=404)
