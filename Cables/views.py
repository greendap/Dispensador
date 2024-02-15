from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
         return render(request, 'Cables/Home.html')

def operario(request):
        return render(request, 'Cables/Operario.html')

def auditor(request):
        return render(request, 'Cables/Auditor.html')

def superA(request):
        return render(request, 'Cables/superA.html')

def manejoProyecto(request):
        return render(request, 'Cables/manejoProyecto.html')

def inforAuditor(request):
        return render(request, 'Cables/inforAuditor.html')

def usuarios(request):
        return render(request, 'Cables/usuarios.html')




