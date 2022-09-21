from django.urls import re_path
from sinaisvitais import views

urlpatterns = [
    re_path(r'^sinaisvitais/$', views.sinaisVitaisApi),
    re_path(r'^sinaisvitais/([0-9]+)$', views.sinaisVitaisApi),
]   