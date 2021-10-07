from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40 , verbose_name='Cliente')
    web = models.URLField(verbose_name='Link')
    logo = models.ImageField(verbose_name='Logo', upload_to='clientes')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
