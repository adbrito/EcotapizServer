from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from .models import *

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
	return HttpResponse(status=404)
