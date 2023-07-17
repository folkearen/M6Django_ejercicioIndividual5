from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request,'home/index.html', {})

def homeContacto(request):
    return render(request, 'home/contacto.html', {})

