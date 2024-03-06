from django.db import models 

class Proyecto(models.Model):
    codigo = models.CharField(primary_key = True, max_length=8)
    nombre = models.CharField(max_length=50)
    cliente = models.CharField(max_length=60)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.codigo) 
