from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from auto import utils
from .models import *
from datetime import date
from django.db.models import Count
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



def cotizacionesXMes(request):
	if request.method=='GET':
		res=[]
		diccionario={}
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-01-')#.annotate(count = Count('fecha'))
		diccionario["label"]="Enero"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		#print(str(len(simulacion))+" \n"+str(diccionario))
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-02-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Febrero"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-03-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Marzo"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-04-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Abril"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-05-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Mayo"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-06-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Junio"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-07-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Julio"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-08-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Agosto"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-09-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Septiembre"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-10-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Octubre"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-11-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Noviembre"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		simulacion=Simulacion.objects.filter(fecha__contains=str(date.today().year)+'-12-')#.annotate(count = Count('fecha'))
		diccionario={}
		diccionario["label"]="Diciembre"
		diccionario["value"]=len(simulacion)
		res.append(diccionario)
		print(res)
		return JsonResponse(res,safe=False)
	return HttpResponse(status=404)
