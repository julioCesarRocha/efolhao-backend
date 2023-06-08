"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path


from rest_framework import routers
from sinaisvitais.api import viewsets as sinaissitaisviewset
from hemodinamica.api import viewsets as hemodinamicaviewset
from usuario.api import viewsets as usuarioviewset
from respiracao.api import viewsets as respiracaoviewset
from neurologico.api import viewsets as neurologicoviewset

route = routers.DefaultRouter()

# route.register(r'sinaisvitais', sinaissitaisviewset.SinaisVitaisViewSet, basename="SinaisVitais")
# route.register(r'hemodinamica', hemodinamicaviewset.HemodinamicaViewSet, basename="Hemodinamica")
# route.register(r'usuario', usuarioviewset.UsuarioViewSet, basename="Usuario")
# route.register(r'respiracao', respiracaoviewset.RespiracaoViewSet, basename="Respiracao")
# route.register(r'neurologico', neurologicoviewset.NeurologicoViewSet, basename="Neurologico")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    re_path(r'^', include('sinaisvitais.urls')),
    re_path(r'^', include('hemodinamica.urls')),
    re_path(r'^', include('usuario.urls')),
    re_path(r'^', include('respiracao.urls')),
    re_path(r'^', include('neurologico.urls')),
]
