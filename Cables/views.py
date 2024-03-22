from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proyecto
from django.contrib.auth.forms import UserCreationForm

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

def prueba(request):
        proyectos = Proyecto.objects.all()
        return render(request, 'Cables/prueba.html', {"proyectos": proyectos})

def login(request):
         return render(request, 'Cables/login.html', {
                 'form' : UserCreationForm
         })

def crearproyectos(request):
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        cliente = request.POST['txtCliente']

        proyecto = Proyecto.objects.create(codigo=codigo, nombre=nombre, cliente=cliente)
        return redirect('/prueba')

def editarProyecto(request, codigo):
        proyecto = Proyecto.objects.get(codigo=codigo)
        return render(request, "Cables/editarProyecto.html", {"proyecto":proyecto})

def modificarProyecto(request):
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        cliente = request.POST['txtCliente']

        proyecto = Proyecto.objects.get(codigo=codigo)
        proyecto.nombre = nombre
        proyecto.cliente = cliente
        proyecto.save()

        return redirect('/prueba')

def eliminarProyecto(request, codigo):
        proyecto = Proyecto.objects.get(codigo=codigo)
        proyecto.delete()
        return redirect('/prueba')



