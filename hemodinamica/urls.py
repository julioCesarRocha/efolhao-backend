from django.urls import re_path
from hemodinamica import views

urlpatterns = [
    re_path(r'^hemodinamica', views.hemodinamicaApi),
    # re_path(r'^hemodinamica', views.hemodinamicaApi),
]   