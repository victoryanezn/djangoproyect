from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, verbose_name="Tipo")
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    color = models.CharField(max_length=50, null=True)
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="NOMBRE:")
    correo = models.EmailField(verbose_name="CORREO:")
    mensaje = models.TextField(verbose_name="MENSAJE:")
    
    def __str__(self):
        return self.nombre
    


class Feedback(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    autor = models.CharField(max_length=10)  # Añadir campo autor
    fecha_creado = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    


# ----------------------------------
#             Chuly
#     GitHub: https://github.com/victoryanezn
#     Discord: chuly2005#0
# ---------------------------------- 