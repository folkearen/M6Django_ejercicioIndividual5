from django.shortcuts import render

# Create your views here.
def mostrarUsuarios(request):
    return render(request,'user_manager/showUsers.html',{})