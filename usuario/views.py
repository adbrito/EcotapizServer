from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from .models import *

# Create your views here.
def getUsuario(request):
	if request.method == 'GET':
		res = []
		usuario= Usuario.objects.filter()
		for usua in usuario:
			#print(usua)

			diccionario={"id":usua.id,"nombre":usua.nombre,"apellido":usua.apellido,
            "correo":usua.correo,"contrasena":usua.contrasena}
			res.append(diccionario)

		return JsonResponse(res,safe=False)
	return HttpResponse(status=404)
