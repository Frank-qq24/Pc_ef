
from django.contrib import admin
from django.urls import path
from miapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/', views.cursos, name = "cursos"),
    path('carreras/', views.carreras, name = "carreras"),
    path('crear_curso/', views.crear_curso, name = "crear_curso"),
    path('crear_carrera/', views.crear_carrera, name = "crear_carrera"),
    path('crear_cursos/', views.crear_cursos, name = "crear_cursos"),
    path('eliminar_curso/<int:id>', views.eliminar_curso, name = "eliminar_curso"),
]
