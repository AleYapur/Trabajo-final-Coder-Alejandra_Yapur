from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
        
         #___________________ Principal
        path('', home, name='home'),
        path('filosofia/', filosofia, name="filosofia"),
        path('acerca/', acerca, name="acerca"),
                       

        #___________________ Productos
        path('productos/', ProductoList.as_view(), name="productos"), 
        path('producto_create/', ProductoCreate.as_view(), name="producto_create"), 
        path('producto_update/<int:pk>/', ProductoUpdate.as_view(), name="producto_update"), 
        path('producto_delete/<int:pk>/', ProductoDelete.as_view(), name="producto_delete"),
        

        #___________________ Clientes
        path('clientes/', ClienteList.as_view(), name="clientes"), 
        path('cliente_create/', ClienteCreate.as_view(), name="cliente_create"), 
        path('cliente_update/<int:pk>/', ClienteUpdate.as_view(), name="cliente_update"), 
        path('cliente_delete/<int:pk>/', ClienteDelete.as_view(), name="cliente_delete"), 

        #_____________________Ordenes
        path('ordenes/', OrdenList.as_view(), name="ordenes"),
        path('orden_create/', OrdenCreate.as_view(), name="orden_create"), 
        path('orden_update/<int:pk>/', OrdenUpdate.as_view(), name="orden_update"), 
        path('orden_delete/<int:pk>/', OrdenDelete.as_view(), name="orden_delete"),
        
              

        #____________________ Busqueda
        path('buscar/', buscarProductos, name="buscar"),
        path('encontrar_productos/', encontrarProductos, name="encontrar_productos"),     
        
        #_____________________Productos individuales
        path('potus/', potus, name="potus"),
        path('anthurium/', anthurium, name="anthurium"),
        path('helecho/', helecho, name="helecho"),
        path('begonia/', begonia, name="begonia"),
        path('palmera_datilera/', palmera_datilera, name="palmera_datilera"),

        #______________________Loguearse, Cerrar sesión, Registrarse

        path('login/', login_request, name="login"),
        path('logout/', user_logout, name="logout"),
        path('registro/', register, name="registro"),

        #____________________ Edicion perfil, Cambio de clave, Avatar
        path('perfil/', editarPerfil, name="perfil"),
        path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
        path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),


]