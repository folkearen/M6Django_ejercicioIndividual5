from django.shortcuts import render, redirect
from .forms import forms
from .models import Usuario
import time
# Create your views here.



def signUp(request):
    if request.method == "POST":
            formulario_post = forms.SignUp(request.POST)
            if formulario_post.is_valid():
                # Guardar el usuario con commit=False para que la contraseña se encripte correctamente
                user = formulario_post.save(commit=False)
                # Asegurarse de que la contraseña se encripte utilizando el método save() personalizado
                user.save()
                return redirect('user_manager:successfulRegistration')

            else:
                # Capturar la excepción de ValidationError y agregar el mensaje de error al formulario
                error_message = None
                if '__all__' in formulario_post.errors:
                    error_message = formulario_post.errors['__all__'][0]
                    return render(request, 'user_manager/signUp.html', {
                        'form': formulario_post,
                        'error': error_message
                    })

    return render(request,'user_manager/signUp.html',{
         'form': forms.SignUp()
        })

    # if request.method == "POST" and request.POST['password'] != request.POST['confirm_password']: 
    #     return render(request,'user_manager/signUp.html',{
    #     'form': forms.signUp(),
    #     'error': 'Las contraseñas no coinciden'
    #     })   

def successfulRegistration(request):
        numero_usuario = Usuario.objects.count()
        return render(request,'user_manager/successfulRegistration.html', {
            'numero_usuario' : numero_usuario 
        } )





# def mostrarUsuarios(request):
#     usuarios =  Usuario.objects.count()
#     return render(request, 'user_manager/showUsers.html', {
#         "usuarios":usuarios
#     })

    # <script>
    #     setTimeout(function() {
    #         window.location.href = '/segunda_pagina/';
    #     }, 5000);  // Redirigir después de 5 segundos (5000 milisegundos)
    # </script>