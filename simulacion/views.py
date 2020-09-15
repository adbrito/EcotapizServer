from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from .models import *

# Create your views here.
def getSimulacion(request):
	if request.method == 'GET':
		res = []
		simulacion= Simulacion.objects.filter()
		for simu in simulacion:
			#print(simu)

			diccionario={"id":simu.id ,"idAuto":simu.idAuto.id,"idDiseno":simu.idDiseno.id,
            "idCotizacion":simu.idCotizacion.id,"idUsuario":simu.idUsuario.id,
			"fecha":simu.fecha,"idMaterial":simu.idMaterial.id}
			res.append(diccionario)

		return JsonResponse(res,safe=False)
	return HttpResponse(status=404)
