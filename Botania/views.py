from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Usuario, tipo_usuario, Catalogo
from .forms import usuarioForm, catalogoForm
from .carrito import Carrito
import requests

# Create your views here.


def indice (request):
    context = {}
    return render(request, 'pages/indice.html', context)

@login_required
def productos (request):
    productos = Catalogo.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'pages/productos.html', context)

def nosotros (request):
    context = {}
    return render(request, 'pages/nosotros.html', context)

@login_required
def suscripcion (request):
    context = {}
    return render(request, 'pages/suscripcion.html', context)

@login_required
def miperfil (request):
    context = {}
    return render(request, 'pages/miperfil.html', context)

def login (request):
    context = {}
    return render(request, 'registration/login.html', context)

@login_required
def carrito(request):
    productos = Catalogo.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'pages/carrito.html', context)

def register(request):
    context ={}
    return render(request, 'registration/register.html', context)

def exit(request):
    logout(request)
    return redirect('indice')

def usuario(request):
    usuario = Usuario.objects.all()
    context = {
        "usuario": usuario
        }
    return render(request, "registration/register.html")

def agregar_usuario(request):
    form = usuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('usuario')
    context = {  
        'form': form
        }
    return render(request, "usuario/agregar.html", context)

def modificar_usuario(request):
    context = { }
    return render(request, "usuario/modificar.html", context)

def eliminar_usuario(request, pk):
   
    return redirect('inicio')

def modificar_usuario(request, pk):
    usuario = Usuario.objects.get(id=pk)
    form = usuarioForm(request.POST or None, instance=usuario)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('miperfil')
    context = {
        "form": form
    }
    return render(request, "pages/miperfil.html", context)

@login_required
def catalogo(request):
    catalogo = Catalogo.objects.all()
    context = {
        "catalogo": catalogo
        }
    return render(request, "catalogo/lista.html", context)

@login_required
def agregar_catalogo(request):
    form = catalogoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogo')
    context = {  'form': form}
    return render(request, "catalogo/agregar.html", context)

@login_required
def modificar_catalogo(request):
    context = { }
    return render(request, "catalogo/modificar.html", context)

@login_required
def eliminar_catalogo(request, pk):
    catalogo = Catalogo.objects.get(id=pk)
    catalogo.delete()
    return redirect('catalogo')

@login_required
def modificar_catalogo(request, pk):
    catalogo = Catalogo.objects.get(id=pk)
    form = catalogoForm(request.POST or None, instance=catalogo)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('catalogo')
    context = {
        "form": form
    }
    return render(request, "catalogo/modificar.html", context)

def agregarP(request, pk):
    carrito = Carrito(request)
    producto = Catalogo.objects.get(id = pk)
    carrito.agregarProd(producto)
    return redirect('carrito')

def eliminarP(request, pk):
    carrito = Carrito(request)
    producto = Catalogo.objects.get(id = pk)
    carrito.eliminarProd(producto)
    return redirect('carrito')

def quitarP(request, pk):
    carrito = Carrito(request)
    producto = Catalogo.objects.get(id = pk)
    carrito.quitarProd(producto)
    return redirect('carrito')

def limpiarP(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito')

def crud(request):
    usuario = Usuario.objects.all()
    context = {
        'usuario' : usuario
    }
    return render(request, 'usuario/lista.html', context)