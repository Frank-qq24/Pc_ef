from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from miapp.models import cours
# Create your views here.
def carreras(request):
    return render(request, 'carreras.html', {
        'titulo':'LISTADO DE CARRERAS'#,
    })

def cursos(request):
    cursos = cours.objects.all()
    return render(request, 'cursos.html', {
        'titulo':'LISTADO DE CURSOS',
        'cursos': cursos
    })

def crear_carrera(request):
    return render(request, 'crear_carrera.html', {
        'titulo':'AGREGAR CARRERA'

    })

def crear_curso(request):
    return render(request, 'crear_curso.html', {
        'titulo':'AGREGAR CURSO',
    })
def eliminar_curso(request, id):
    curso =  cours.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')
# creamos estudiantes
def crear_cursos(request):
    curso=cours(
    idcourse= "1",
    code    = "69788869",
    name    = "programacion",
    hour    = "8",
    credits = "6",
    state   = "A"
    )
    curso.save()
    return HttpResponse (f"<h1>Estudiante registrado:</h1> "+
    f"<br> <b>id:</b> {curso.idcourse} <br> <b>codigo:</b> {curso.code} <br> <b>Nombre:</b> {curso.name} <br> "+
    f"<b>horas:</b> {curso.hour} <br> <b>Creditos:</b> {curso.credits}"+
    f"<br> <b>Estado:</b> {curso.state}")
    