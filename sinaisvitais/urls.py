from django.urls import re_path
from sinaisvitais import views

urlpatterns = [
    re_path(r'^sinaisvitais/(?P<id_usuario>[-\w]+)/?$', views.sinaisVitaisApi),
    re_path(r'^sinaisvitais', views.sinaisVitaisApi),
]   