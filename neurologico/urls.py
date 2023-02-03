from django.urls import re_path
from neurologico import views

urlpatterns = [
    re_path(r'^neurologico', views.neurologicoApi),
]   