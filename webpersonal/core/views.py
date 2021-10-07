from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"core/index.html")

def contacto(request):
        return render(request,"core/contact.html")
