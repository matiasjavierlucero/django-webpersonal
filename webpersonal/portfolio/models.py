from django.db import models


class Categoria(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    created = models.DateField(auto_now_add=True, verbose_name='Creado el')
    updated = models.DateField(auto_now=True, verbose_name='Actualizado el')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'categoria'  # NOMBRE QUE QUIERO QUE ME APAREZCA EN LA LISTA
        verbose_name_plural = 'categorias'
        ordering = ["-created"]


class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField( verbose_name='Descripcion')
    image = models.ImageField( verbose_name='Imagen', upload_to="portfolio")
    created = models.DateField(auto_now_add=True,  verbose_name='Creado el')
    updated = models.DateField(auto_now=True, verbose_name='Actualizado el')
    url = models.URLField(null=True, blank=True)
    categoria =models.ForeignKey(Categoria,verbose_name='Categoria', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'portafolios' #NOMBRE QUE QUIERO QUE ME APAREZCA EN LA LISTA
        verbose_name_plural = 'portafolios'
        ordering = ["-created"]



    def __str__(self):
        return self.title
