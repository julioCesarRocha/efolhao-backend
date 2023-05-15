from django.urls import re_path
from sinaisvitais import views

urlpatterns = [
    re_path(r'^sinaisvitais', views.sinaisVitaisApi),
    re_path('sinaisvitais/<string:id_sinal_vital>/', views.sinaisVitaisApi, name='sinaisVitaisApi'),
]   