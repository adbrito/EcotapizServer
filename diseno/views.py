from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from .models import *
from auto import utils

# Create your views here.
def getDiseno(request):
	if request.method == 'GET':
		res = []
		diseno= Diseno.objects.filter()
		for dise in diseno:
			#print(dise)

			diccionario={"id":dise.id,"nombre":dise.nombre,"descripcion":dise.descripcion,
            "imagen":dise.imagen,"metros":dise.metros,"ranking":dise.ranking,"glb":dise.glb}
			res.append(diccionario)

		return JsonResponse(res,safe=False)

	elif (request.method == 'POST'):
		body = utils.request_todict(request)
		nombre = body.get("nombre", None)
		descripcion = body.get("descripcion", None)
		imagen = body.get("imagen", None)
		metros = body.get("metros",None)
		ranking = body.get("ranking", None)
		glb = body.get("glb", None)
		try:
			diseno = Diseno().crearDiseno(nombre,descripcion,imagen,metros,ranking,glb)
			return JsonResponse({
                'STATUS' : 'OK',
                'CODIGO' : 200,
                'DETALLE' :  utils.response_message("Diseno","creado",diseno)
            })
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method,"diseno",e)
            })

	elif (request.method == 'PUT'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		nombre = body.get("nombre", None)
		descripcion = body.get("descripcion", None)
		imagen = body.get("imagen", None)
		metros = body.get("metros",None)
		ranking = body.get("ranking", None)
		glb = body.get("glb", None)
		try:
			diseno = Diseno().actualizarDiseno(id,nombre,descripcion,imagen,metros,ranking,glb)
			if diseno:
				return JsonResponse({
                	'STATUS' : 'OK',
                	'CODIGO' : 200,
                	'DETALLE' :  utils.response_message("Diseno","actualizado",diseno)
            	})
			else:
				return JsonResponse({
                	'STATUS' : 'Error',
                	'CODIGO' : 404,
                	'DETALLE' :  utils.error_message_1("Diseno",id)
            	})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "diseno",e)
            })
	
	elif(request.method == 'DELETE'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		try:
			mensaje = Diseno().eliminarDiseno(id)
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
                	'DETALLE' : utils.error_message_1("Diseno",id)
           		})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "diseno",e)
            })
	else:
		return HttpResponse(status=404)
