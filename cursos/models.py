from django.db import models
import uuid
# Create your models here.

class Curso(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True,null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __strt__(self):
        return self.nombre