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
		#print("Nombre: "+str(nombre))
		descripcion = body.get("descripcion", None)
		glb = body.get("glb", None)
		imagen = body.get("imagen", None)
		ranking = body.get("ranking", None)
		try:
			nuevo_auto = Auto().crearAuto(nombre, descripcion, glb, imagen, ranking)
			return JsonResponse({
                'STATUS' : 'OK',
                'CODIGO' : 200,
                'DETALLE' :  'El objeto Auto creado tiene los siguientes atributos: ' + str(nuevo_auto.nombre)
				+ '-' + str(nuevo_auto.descripcion) + '-' + str(nuevo_auto.glb) + '-' + str(nuevo_auto.imagen) + 
				'-' + str(nuevo_auto.ranking)
            })
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : 'Error creando auto' + str(e)
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
			return JsonResponse({
                'STATUS' : 'OK',
                'CODIGO' : 200,
                'DETALLE' :  'El objeto Auto actualizado tiene los siguientes atributos: ' + str(nuevo_auto.nombre)
				+ '-' + str(nuevo_auto.descripcion) + '-' + str(nuevo_auto.glb) + '-' + str(nuevo_auto.imagen) + 
				'-' + str(nuevo_auto.ranking)
            })
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : 'Error actualizando auto' + str(e)
            })
	
	elif(request.method == 'DELETE'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		try:
			mensaje = Auto().eliminarAuto(id)
			return JsonResponse({
                'STATUS' : 'OK',
                'CODIGO' : 200,
                'DETALLE' :  mensaje
            })
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : 'Error actualizando auto' + str(e)
            })

	else:
		return HttpResponse(status=404)
