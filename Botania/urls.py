from django.urls import path
from . import views

urlpatterns = [
    path('indice', views.indice, name='indice'),
    path('productos', views.productos, name='productos'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('suscripcion', views.suscripcion, name='suscripcion'),
    path('miperfil', views.miperfil, name='miperfil'),
    path('login', views.login, name='login'),
    path('carrito', views.carrito, name='carrito'),
    path('register', views.register, name='register'),
    path('logout/', views.exit, name='exit'),
    path('usuario/', views.usuario, name='usuario'),
    path('usuario/agregar', views.agregar_usuario, name='agregar_usuario'),
    path('usuario/modificar', views.modificar_usuario, name='modificar_usuario'),
    path('eliminar/<str:pk>', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuario/modificar/<str:pk>', views.modificar_usuario, name='modificar_usuario'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('catalogo/agregar', views.agregar_catalogo, name='agregar_catalogo'),
    path('catalogo/modificar', views.modificar_catalogo, name='modificar_catalogo'),
    path('eliminar/<str:pk>', views.eliminar_catalogo, name='eliminar_catalogo'),
    path('catalogo/modificar/<str:pk>', views.modificar_catalogo, name='modificar_catalogo'),
    path('agregarProd/<int:pk>/', views.agregarP, name='agregarP'),
    path('eliminarProd/<int:pk>/', views.eliminarP, name='eliminarP'),
    path('quitarProd/<int:pk>/', views.quitarP, name='quitarP'),
    path('limpiar/', views.limpiarP, name='limpiarP'),
]