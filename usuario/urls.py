from django.urls import re_path
from usuario import views

urlpatterns = [
    re_path(r'^usuario', views.usuarioApi),
]   