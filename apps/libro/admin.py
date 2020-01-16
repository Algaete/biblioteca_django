from django.contrib import admin
from .models import Autor
from .models import Libro

admin.site.register(Autor)
admin.site.register(Libro)
