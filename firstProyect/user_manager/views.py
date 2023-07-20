from django.shortcuts import render
from .forms import forms
# Create your views here.


def mostrarUsuarios(request):
    if request.method == "POST" and request.POST['password'] != request.POST['confirm_password']: 
        return render(request,'user_manager/showUsers.html',{
        'form': forms.signUp(),
        'error': 'Las contraseñas no coinciden'
        })
        
    elif request.method == "POST":
        formulario_post = forms.signUp(request.POST)
        if formulario_post.is_valid():
            formulario_post.save()

    return render(request,'user_manager/showUsers.html',{
         'form': forms.signUp()
        })