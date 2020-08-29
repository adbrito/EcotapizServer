from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from .models import *

# Create your views here.
def getCotizacion(request):
	if request.method == 'GET':
		res = []
		cotizacion= Cotizacion.objects.filter()
		for coti in cotizacion:
			#print(coti)

			diccionario={"id":coti.id,"subtotal":coti.subtotal,"total":coti.total,
            "iva":coti.iva}
			res.append(diccionario)

		return JsonResponse(res,safe=False)
	return HttpResponse(status=404)
