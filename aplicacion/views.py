from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import * 


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, "aplicacion/index.html")  

def filosofia(request):
    return render(request, "aplicacion/filosofia.html") 

def acerca(request):
    return render(request, "aplicacion/acerca.html")  


@login_required
def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto) 

@login_required
def ordenes(request):
    contexto = {'ordenes': Orden.objects.all().order_by("orden_id")}
    return render(request, "aplicacion/ordenes.html", contexto) 

def productos(request):
    contexto = {'productos': Producto.objects.all().order_by("id")}
    return render(request, "aplicacion/productos.html", contexto) 



#_______________________________________ Buscar productos

def buscarProductos(request):
    return render(request, "aplicacion/buscar.html")

def encontrarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"productos": productos}
        return render(request, "aplicacion/productos.html", contexto)
    

    contexto = {'productos': Producto.objects.all()}
    return render(request, "aplicacion/productos.html", contexto) 


#________________________________________ Clientes
class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ["id", "nombre", "apellido", "email"]
    success_url = reverse_lazy("clientes")

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ["id", "nombre", "apellido", "email"]
    success_url = reverse_lazy("clientes")

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")


#__________________________________________ Productos
class ProductoList(LoginRequiredMixin, ListView):
    model = Producto

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ["id", "nombre", "precio", "descripcion"]
    success_url = reverse_lazy("productos")

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ["id", "nombre", "precio", "descripcion"]
    success_url = reverse_lazy("productos")

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("productos")    

#____________Órdenes

class OrdenList(LoginRequiredMixin, ListView):
    model = Orden

class OrdenCreate(LoginRequiredMixin, CreateView):
    model = Orden
    fields = ["orden_id", "productos", "cantidad", "valor_total", "direccion_envio", "estado"]
    success_url = reverse_lazy("ordenes")

class OrdenUpdate(LoginRequiredMixin, UpdateView):
    model = Orden
    fields = ["orden_id", "productos", "cantidad", "valor_total", "direccion_envio", "estado"]
    success_url = reverse_lazy("ordenes")

class OrdenDelete(LoginRequiredMixin, DeleteView):
    model = Orden
    success_url = reverse_lazy("ordenes")



#________________________ Loguearse, Cerrar sesión, Registrarse
def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
             #______ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            #________________________________________________________
            
            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} )    

@login_required
def user_logout(request):
    logout(request)
    return render(request, "aplicacion/logout.html", {})


#_______________________________________ Edición de perfil

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editar_perfil.html", {"form": miForm} )    
   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #___ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AvatarForm()

    return render(request, "aplicacion/agregar_avatar.html", {"form": miForm} )      

#___________________________________Productos individuales

def potus(request):
    return render(request, "aplicacion/potus.html") 

def anthurium(request):
    return render(request, "aplicacion/anthurium.html") 

def helecho(request):
    return render(request, "aplicacion/helecho.html") 


def begonia(request):
    return render(request, "aplicacion/begonia.html") 

def palmera_datilera(request):
    return render(request, "aplicacion/palmera_datilera.html") 



