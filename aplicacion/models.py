from django.db import models
from django.contrib.auth.models import User



class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)    
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    precio_descuento = models.FloatField(blank=True, null=True)
    imagen = models.ImageField(blank=True, null=True)
       
    
    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}"  
    
    

#________________Clientes

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"
    
    def __str__(self):
        return f"{self.user} {self.imagen}"



# __________________________ Ordenes


ORDER_STATUS_CHOICES = (
    ('Creada','creada'),
    ('Pagada','pagada'),
    ('Enviada','enviada'),
    
)

class Orden(models.Model):
    """
    """
    orden_id = models.IntegerField(primary_key=True)
    productos = models.CharField(max_length=120)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    estado = models.CharField(max_length=120,default='creada',choices=ORDER_STATUS_CHOICES)    
    valor_total = models.DecimalField(default=0,max_digits=100,decimal_places=2)
    direccion_envio = models.CharField(max_length=150,blank=True, null=True)
    fecha = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
    class Meta:
        verbose_name = "Órden"
        verbose_name_plural = "Órdenes"
    
    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return self.orden_id


