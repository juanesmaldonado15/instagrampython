from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *
# Create your views here.

def registro (request):
    return render (request,'registro.html')

def crear_usuario (request):

    Nombre_completo = request.POST['NombreCompleto']
    Correo_electronico = request.POST['CorreoElectronico']
    Usuario = request.POST['Usuario']
    Contrasena = request.POST['Contrasena']
    Confirmar_contrasena = request.POST['ConfirmarContrasena']
    if Contrasena == Confirmar_contrasena:
        print (Nombre_completo)
        print (Correo_electronico)
        print (Usuario)
        print (Contrasena)
        print (Confirmar_contrasena)
        user=User.objects.create_user(username = Usuario, email = Correo_electronico, first_name = Nombre_completo, password= Contrasena)
        myUser = MiUsuario( usuario = user )
        myUser.save

        print (user)
        print (user.password)

        return redirect('ingresar')
    else:
        return redirect('registro')

def ingresar (request):
    return render (request,'ingresar.html')

def inicio(request):
    return render (request,'inicio.html')
