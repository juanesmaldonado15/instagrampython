from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
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

def ingresar(request):
    return render (request,'ingresar.html')

@login_required
def uploadFile(request):
    curr_user = request.user
    post_user = post.objects.filder(creador=curr_user.id).count();
    madiaFile = request.FILES[ 'photo' ]
    newNameFile = curr_user.username +  "-" + str(curr_user.id + "-") + str(post_user);
    fs = FileSystemStorage()
    filename =  fs.save(newNameFile, mediaFile)
    uploaded_file_url = fs.url(filename)
    photo = uploaded_file_url;
    description = request.POST[ 'description' ];
    newPost = Post( foto = photo, descripcion = description, creador = curr_user );
    newPost.save();
    media_user = Post.objects.filter( creador = curr_user.id );
    context = { 'curr_user' : curr_user, 'media_user' : media_user }
    return render (request, 'instagram/profile.html', context)

def inicio(request):
    return render (request,'inicio.html')

def perfil(request):
    return render (request,'perfil.html')

def subirfoto(request):
    return render (request,'subirfoto.html')
