from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from .models import *
from auto import utils

# Create your views here.
def getMaterial(request):
	if request.method == 'GET':
		res = []
		material= Material.objects.filter()
		for mate in material:
			#print(mate)

			diccionario={"id":mate.id,"nombre":mate.nombre,"descripcion":mate.descripcion,
            "imagen":mate.imagen,"ranking":mate.ranking,"precio":mate.precio}
			res.append(diccionario)

		return JsonResponse(res,safe=False)

	elif (request.method == 'POST'):
		body = utils.request_todict(request)
		nombre = body.get("nombre", None)
		descripcion = body.get("descripcion", None)
		imagen = body.get("imagen", None)
		ranking = body.get("ranking", None)
		precio = body.get("precio", None)
		try:
			material = Material().crearMaterial(nombre, descripcion, imagen, ranking,precio)
			return JsonResponse({
                'STATUS' : 'OK',
                'CODIGO' : 200,
                'DETALLE' :  utils.response_message("Material","creado",material.to_string())
            })
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method,"material",e)
            })

	elif (request.method == 'PUT'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		nombre = body.get("nombre", None)
		descripcion = body.get("descripcion", None)
		imagen = body.get("imagen", None)
		ranking = body.get("ranking", None)
		precio = body.get("precio", None)
		try:
			material = Material().actualizarMaterial(id,nombre, descripcion, imagen, ranking,precio)
			if material:
				return JsonResponse({
                	'STATUS' : 'OK',
                	'CODIGO' : 200,
                	'DETALLE' :  utils.response_message("Material","actualizado",material.to_string())
            	})
			else:
				return JsonResponse({
                	'STATUS' : 'Error',
                	'CODIGO' : 404,
                	'DETALLE' :  utils.error_message_1("Material",id)
            	})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "material",e)
            })
	
	elif(request.method == 'DELETE'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		try:
			mensaje = Material().eliminarMaterial(id)
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
                	'DETALLE' : utils.error_message_1("Material",id)
           		})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "material",e)
            })

	else:
		return HttpResponse(status=404)

def getOneMaterial(request,pk):
	if request.method == 'GET':
		diccionario = {}
		material = Material.objects.get(pk=pk)
		if material:
			diccionario = {"material" : material.nombre}
		return JsonResponse(diccionario,safe=False)
	else:
		return HttpResponse(status=404)