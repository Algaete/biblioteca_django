from django.urls import path,re_path
from .views import crearAutor,ListarAutor,editarAutor,eliminarAutor


urlpatterns = [
    path('crear_autor/',crearAutor, name = 'crear_autor'),
    path('listar_autor',ListarAutor, name ='listar_autor'),
    path('editar_autor/<int:id>',editarAutor, name = 'editar_autor'),
    path('eliminar_autor/<int:id>',eliminarAutor, name = 'eliminar_autor')
]
