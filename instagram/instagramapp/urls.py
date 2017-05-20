from django.conf.urls import url

from . import views

urlpatterns=[
  url(r'^$', views.registro, name = 'registro'),
   url(r'^$', views.registro, name = 'ingresar'),
  url(r'crear_usuario/$', views.crer_usuario, name= 'crear_usuario'),

]
s
