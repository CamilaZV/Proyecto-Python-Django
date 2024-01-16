from django.shortcuts import render, redirect
from .models import Estudiante, Carrera, Curso
from . forms import UsuarioForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here
def home(request):
    return render(request, "home.html")

def registroUsuario(request): 
    if request.method=='GET':
        return render(request, 'registroUsuario.html', { 
            'form' : UsuarioForm 
        })
    else:
        if request.POST['password1']!=request.POST['password2']:
            return render(request, 'registroUsuario.html', { 
            'form' : UsuarioForm,
            'mensaje' : 'Las contraseñas no coinciden.'
        })
        else:
            try:
                user = User.objects.create_user(username=request.POST['nombre_usuario'], email=request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'registroUsuario.html', { 
                    'form' : UsuarioForm,
                    'mensaje' : 'Usuario registrado correctamente.'
                })
            except IntegrityError:
                return render(request, 'registroUsuario.html', { 
                    'form' : UsuarioForm,
                    'mensaje' : 'El usuario ya existe.'
                })
        
def iniciarSesion(request): 
    if request.method == 'GET':
        return render(request, 'iniciarSesion.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña no válido.'
                })
        else:
            login(request, user)
            return redirect('/home/')

def cerrarSesion(request):
    logout(request)
    return redirect('/iniciarSesion/')

def gestionCursos(request):
    listaCursos = Curso.objects.all()
    return render(request, "gestionCursos.html",{"cursos": listaCursos})

def registrarCurso(request):   
    try:
        codigo=request.POST['txtCodigo']
        nombre=request.POST['txtNombre']
        creditos=request.POST['numCreditos']
        docente=request.POST['txtDocente']
        Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, docente=docente)
        return redirect('/gestionCursos/')
    except:
         listaCursos = Curso.objects.all()
         return render(request, "gestionCursos.html",{"cursos": listaCursos , 'error' : 'Ya existe un curso con este código!'})

def edicionCurso(request,codigo): 
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    docente=request.POST['txtDocente']
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.docente = docente
    curso.save()
    return redirect('/gestionCursos/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/gestionCursos/')

def consultaCarreras(request):
    listaCarreras = Carrera.objects.all()
    return render(request, "consultaCarreras.html",{"carreras": listaCarreras})

def gestionEstudiantes(request):
    listaEstudiantes = Estudiante.objects.all()
    listaCarreras = Carrera.objects.all()
    return render(request, "gestionEstudiantes.html",{"estudiantes": listaEstudiantes,"carreras": listaCarreras})

def registrarEstudiante(request):
    try:
        dni=request.POST['txtDni']
        apellido=request.POST['txtApellido']
        nombre=request.POST['txtNombreE']
        fechaNacimiento=request.POST['txtFechaNacimiento']
        sexo=request.POST['txtSexo']
        carrera=request.POST['txtCarrera']
        Estudiante.objects.create(dni=dni, apellido=apellido, nombre=nombre, fechaNacimiento=fechaNacimiento, 
                                            sexo=sexo, carrera=Carrera.objects.get(codigo=carrera))
        return redirect('/gestionEstudiantes/')
    except:
        listaEstudiantes = Estudiante.objects.all()
        listaCarreras = Carrera.objects.all()
        return render(request, "gestionEstudiantes.html",{"estudiantes": listaEstudiantes,"carreras": listaCarreras,
           'error': 'Ya existe un estudiante con esta identificación!'
        })

