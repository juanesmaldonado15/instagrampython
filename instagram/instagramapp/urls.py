from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns=[
  url(r'^$', views.registro, name='registro'),
  url(r'^crear_usuario/$', views.crear_usuario, name= 'crear_usuario'),
  url(r'^inicio/$', views.inicio, name= 'inicio'),
  url(r'^perfil/$', views.perfil, name= 'perfil'),

  url(r'^login/$', auth_views.LoginView.as_view(template_name='ingresar.html',redirect_authenticated_user=True), name='login'),
  url(r'^logout/$', auth_views.LogoutView.as_view(template_name='ingresar.html'), name='logout'),
  ]
