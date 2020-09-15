from django.urls import path
from .views import *


urlpatterns = [
	path('cotizacion/', getCotizacion),
	path('queryCotizacion/',clienteCotizacion),
]
