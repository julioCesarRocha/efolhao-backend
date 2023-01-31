from django.urls import re_path
from respiracao import views

urlpatterns = [
    re_path(r'^respiracao', views.respiracaoApi),
]   