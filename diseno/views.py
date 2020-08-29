from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from .models import *

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
	return HttpResponse(status=404)
