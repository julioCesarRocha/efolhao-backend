from django.urls import re_path
from usuario import views

urlpatterns = [
    re_path(r'^usuario', views.usuarioApi),
    # re_path(r'^usuario/(?P<id_usuario>[-\w]+)/$', views.usuarioApi),
    re_path(r'^usuario/<str:id_usuario>', views.usuarioApi),
]   