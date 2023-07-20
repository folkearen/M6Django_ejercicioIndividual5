from django.shortcuts import render
from .forms import forms
from .models import Usuario
# Create your views here.


def signUp(request):
    # if request.method == "POST" and request.POST['password'] != request.POST['confirm_password']: 
    #     return render(request,'user_manager/signUp.html',{
    #     'form': forms.signUp(),
    #     'error': 'Las contraseñas no coinciden'
    #     })
        
    if request.method == "POST":
        formulario_post = forms.SignUp(request.POST)
        if formulario_post.is_valid():
            # Guardar el usuario con commit=False para que la contraseña se encripte correctamente
            user = formulario_post.save(commit=False)
            # Asegurarse de que la contraseña se encripte utilizando el método save() personalizado
            user.save()

    return render(request,'user_manager/signUp.html',{
         'form': forms.SignUp()
        })

def mostrarUsuarios(request):
    usuarios =  Usuario.objects.all()
    return render(request, 'user_manager/showUsers.html', {
        "usuarios":usuarios
    })