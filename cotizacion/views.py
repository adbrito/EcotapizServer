from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from auto import utils
from .models import *
from datetime import date
from simulacion.models import Simulacion

# Create your views here.
def getCotizacion(request):
	if request.method == 'GET':
		res = []
		cotizacion= Cotizacion.objects.filter().order_by('-total')
		for coti in cotizacion:
			#print(coti)

			diccionario={"id":coti.id,"subtotal":coti.subtotal,"total":coti.total,
            "iva":coti.iva}
			res.append(diccionario)

		return JsonResponse(res,safe=False)
	elif (request.method == 'POST'):
		body = utils.request_todict(request)
		subtotal = body.get("subtotal", None)
		total = body.get("total", None)
		iva = body.get("iva", None)
		try:
			cotizacion = Cotizacion().crearCotizacion(subtotal,total,iva)
			return JsonResponse({
                'STATUS' : 'OK',
                'CODIGO' : 200,
                'DETALLE' :  utils.response_message("Cotizacion", "creado",cotizacion.to_string())
            })
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method,"cotizacion",e)
            })

	elif (request.method == 'PUT'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		subtotal = body.get("subtotal", None)
		total = body.get("total", None)
		iva = body.get("iva", None)
		try:
			cotizacion = Cotizacion().actualizarCotizacion(id,subtotal,total,iva)
			if cotizacion:
				return JsonResponse({
                	'STATUS' : 'OK',
                	'CODIGO' : 200,
                	'DETALLE' : utils.response_message("Cotizacion", "actualizado",cotizacion.to_string())
            	})
			else:
				return JsonResponse({
                	'STATUS' : 'Error',
                	'CODIGO' : 404,
                	'DETALLE' :  utils.error_message_1("Cotizacion",id)
            	})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method,"cotizacion",e)
            })
	
	elif(request.method == 'DELETE'):
		body = utils.request_todict(request)
		id = body.get("id",None)
		try:
			mensaje = Cotizacion().eliminarCotizacion(id)
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
                	'DETALLE' :  utils.error_message_1("Cotizacion",id)
           		})
		except Exception as e:
			return JsonResponse({
                'STATUS' : 'ERROR',
                'CODIGO' : 400,
                'DETALLE' : utils.error_message_2(request.method,"cotizacion",e)
            })

	else:
		return HttpResponse(status=404)





def clienteCotizacion(request):
	if request.method=='GET':
		print(date.today())
		res=[]
		simulacion= Simulacion.objects.filter(fecha=date.today())#.order_by('-fecha')[:2]#.values('total').annotate(total=Count('total')).order_by('fecha')
		for i in simulacion:
			
			diccionario={"totalCotizacion":i.idCotizacion.total,"cliente":i.idUsuario.nombre+" "+i.idUsuario.apellido,"fecha":i.fecha}
			res.append(diccionario)
		print(res)
		return JsonResponse(res,safe=False)
	return HttpResponse(status=404)

