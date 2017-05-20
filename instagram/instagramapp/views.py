from django.shortcuts import render

# Create your views here.

def registro (request):
    return render (request,'registro.html')

def crear_usuario (request):

    Nombre completo = request.POST['Nombre completo']
    Correo electronico = request.POST['Correo electrónico']
    Usuario = request.POST['Usuario']
    Contraseña = request.POST['Contraseña']
    Confirmar contraseña = request.POST['Confirmar contraseña']



     print (Nombre completo)
     print (Correo electrónico)
     print (Usuario)
     print (Contraseña)
     print (Confirmar contraseña)

def registro (request):
    return render (request,'ingresar.html')
