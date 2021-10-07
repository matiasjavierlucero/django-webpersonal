from django.shortcuts import render
from .models import Cliente
# Create your views here.
def about(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/about.html",{'clientes':clientes})
