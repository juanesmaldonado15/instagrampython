from django.conf.urls import url

from . import views

urlpatterns=[
  url(r'^$', views.registro, name='registro'),
  url(r'^ingresar/$', views.ingresar, name = 'ingresar'),
  url(r'^crear_usuario/$', views.crear_usuario, name= 'crear_usuario'),
  url(r'^inicio/$', views.inicio, name= 'inicio'),

  ]
