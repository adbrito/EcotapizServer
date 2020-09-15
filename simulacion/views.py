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


def getSimulaciones(request, id):
	#print(id)
	res = []
	simulacion = Simulacion.objects.all()
	for simu in simulacion:
        #if simu:
        #print(simu.idAuto.id)
		if(id == simu.idUsuario.id):
			diccionario = {
				"id": simu.id,
				"idAuto": simu.idAuto.id,
				"idDiseno": simu.idDiseno.id,
				"idCotizacion": simu.idCotizacion.id,
				"idUsuario": simu.idUsuario.id,
				"fecha": simu.fecha,
				"idMaterial": simu.idMaterial.id
			}
			res.append(diccionario)

	return JsonResponse(res,safe=False)



# Create your views here.
def getSimulaciones(request, id):
	#print(id)
	res = []
	simulacion = Simulacion.objects.all()

	#Cada simu es un Auto Object (instancia del diccionario simulacion)
	for simu in simulacion:
        #if simu:
        #print(simu.idAuto.id)
		if(id == simu.idUsuario.id):
			#Obtenemos las descripciones de cada campo
			#print(simu.idAuto.descripcion)

			#autosDB = Auto.objects.filter(id = simu["idAuto"])
			#print(autosDB[0].descripcion)
			
			diccionario = {
				"id": simu.id,
				"Auto": simu.idAuto.descripcion,
				"Diseno": simu.idDiseno.descripcion,
				"Cotizacion": simu.idCotizacion.total,
				"Usuario": simu.idUsuario.nombre,
				"fecha": simu.fecha,
				"Material": simu.idMaterial.descripcion
			}
			res.append(diccionario)

	return JsonResponse(res,safe=False)





def getSimulacion(request):
<<<<<<< HEAD
	#Prueba
	if request.method == 'GET':
		res = []
		simulacion= Simulacion.objects.all()
		for simu in simulacion:
			#if simu:
				print(simu.idAuto.id)
=======
    body = utils.request_todict(request)
    idUsuario = body.get("idUsuario", None)

    print(idUsuario)
    if request.method == 'GET':
        res = []
        simulacion= Simulacion.objects.all()
        for simu in simulacion:
            #if simu:
            #print(simu.idAuto.id)

            diccionario={"id":simu.id ,"idAuto":simu.idAuto.id,"idDiseno":simu.idDiseno.id,
                     "idCotizacion":simu.idCotizacion.id,"idUsuario":simu.idUsuario.id,
            "fecha":simu.fecha,"idMaterial":simu.idMaterial.id}
            res.append(diccionario)

        return JsonResponse(res,safe=False)


>>>>>>> Get filtrado simulaciones para usuario

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
