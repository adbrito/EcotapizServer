from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
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


