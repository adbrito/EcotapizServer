from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from .models import *

# Create your views here.
def getAuto(request):
	if request.method == 'GET':
		res = []
		auto= Auto.objects.filter()
		for aut in auto:
			#print(aut)

			diccionario={"id":aut.id,"nombre":aut.nombre,"descripcion":aut.descripcion,
            "glb":aut.glb, "imagen":aut.imagen, "ranking":aut.ranking}
			res.append(diccionario)

		return JsonResponse(res,safe=False)
	return HttpResponse(status=404)
