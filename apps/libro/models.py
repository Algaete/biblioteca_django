from django.db import models

# Create your models here.
class Autor(models.Model):
    #django pone claves orimearias por default u autoincremental si no la especificamos
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False,  null = False)
    apellidos = models.CharField(max_length = 220, blank = False,  null = False)
    nacionalidad = models.CharField(max_length = 100, blank = False,  null = False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

# manera en q se identifica cada objeto en el admin, en este caso con el nombre
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Título',max_length = 255,blank = False, null = False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank = False, null = False)
    # relacion 1 a 1 es OneToOneField necesita on_delete = models.CASCADE, para uno a muchos poner ForeignKey necesita on_delete = models.CASCADE, y para muchos a muchos es ManyToManyField
    autor_id = models.ManyToManyField(Autor)
    # campo se actualiza solo o se crea solo
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
