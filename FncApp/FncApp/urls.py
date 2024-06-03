"""
URL configuration for FncApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fincal.views import calculadora, get_number, currency_c, tasa_cambio, subir_archivo, actualizaPrecios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calculadora, name='Calc'),
    path('resultado/', get_number, name='result'),
    path('convert/', currency_c, name='exchange'),
    path('exchange/', tasa_cambio, name='currency'),
    path('success/', subir_archivo),
    path('valormoneda/', actualizaPrecios, name='valormoneda')
]
