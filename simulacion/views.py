from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from auto.models import Auto
from diseno.models import Diseno
from cotizacion.models import Cotizacion
from material.models import Material
from usuario.models import Usuario
import requests
from .models import *
from auto import utils

# Create your views here.
def getSimulacion(request):
	#Prueba
	if request.method == 'GET':
		res = []
		simulacion= Simulacion.objects.all()
		for simu in simulacion:
			#if simu:
				print(simu.idAuto.id)

				diccionario={"id":simu.id ,"idAuto":simu.idAuto.id,"idDiseno":simu.idDiseno.id,
            	"idCotizacion":simu.idCotizacion.id,"idUsuario":simu.idUsuario.id,
				"fecha":simu.fecha,"idMaterial":simu.idMaterial.id}
				res.append(diccionario)

		return JsonResponse(res,safe=False)
	elif (request.method == 'POST'):
		body = utils.request_todict(request)
		idAuto = body.get("idAuto", None)
		idDiseno = body.get("idDiseno", None)
		idCotizacion = body.get("idCotizacion", None)
		idUsuario = body.get("idUsuario",None)
		fecha = body.get("fecha", None)
		idMaterial = body.get("idMaterial", None)
		try:
			simulacion = Simulacion().crearSimulacion(idAuto,idDiseno,idCotizacion,idUsuario,fecha,idMaterial)
			return JsonResponse({
                'STATUS' : 'OK',
                'CODIGO' : 200,
                'DETALLE' :  utils.response_message("Simulacion","creado",simulacion.to_string())
            })
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method,"simulacion",e)
            })

	elif (request.method == 'PUT'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		idAuto = body.get("idAuto", None)
		idDiseno = body.get("idDiseno", None)
		idCotizacion = body.get("idCotizacion", None)
		idUsuario = body.get("idUsuario",None)
		fecha = body.get("fecha", None)
		idMaterial = body.get("idMaterial", None)
		try:
			simulacion = Simulacion().actualizarSimulacion(id,idAuto,idDiseno,idCotizacion,idUsuario,fecha,idMaterial)
			if simulacion:
				return JsonResponse({
                	'STATUS' : 'OK',
                	'CODIGO' : 200,
                	'DETALLE' :  utils.response_message("Simulacion","actualizado",simulacion.to_string())
            	})
			else:
				return JsonResponse({
                	'STATUS' : 'Error',
                	'CODIGO' : 404,
                	'DETALLE' :  utils.error_message_1("Simulacion",id)
            	})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "simulacion",e)
            })
	
	elif(request.method == 'DELETE'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		try:
			mensaje = Simulacion().eliminarSimulacion(id)
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
                	'DETALLE' : utils.error_message_1("Simulacion",id)
           		})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method, "simulacion",e)
            })
	else:
		return HttpResponse(status=404)
