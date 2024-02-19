from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm, TaskSobrepeso, TaskLocalidad, TaskCurso
from .models import Task, Sobrepeso, Localidad, Curso
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

# Vista de inicio
def home(request):
    return render(request, 'home.html')

# Vista de creación e inicio de usuario
def singup(request):

    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'singup.html', {
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })

# Vista de tareas
#El login_required indica a la pag que se requiere estar logueado para poder acceder a dicha vista
@login_required
def task(request):
    return render(request, 'task.html',)

# Vista de creación de los "Tasks"
@login_required
def create_task(request):
    # GET cuando se ingresa primero a la página
    match request.method:
        case 'GET':
            return render(request, 'create_task.html', {
                'formS': TaskSobrepeso,
                'formL': TaskLocalidad,
                'formC': TaskCurso,
                'form': TaskForm,
            })
        case 'POST':
            try:
                #Se cargan los datos de los formularios
                form_sobrepeso = TaskSobrepeso(request.POST, instance=Sobrepeso())
                form_localidad = TaskLocalidad(request.POST, instance=Localidad())
                form_curso = TaskCurso(request.POST, instance=Curso())
                form_datos_generales = TaskForm(request.POST, instance=Task())
                
                if form_sobrepeso.is_valid and form_localidad.is_valid and form_datos_generales.is_valid and form_curso.is_valid:
                    #Se guardan los datos del formulario en su respectiva tabla (BD)
                    task2 = form_sobrepeso.save()
                    task3 = form_localidad.save()
                    task4 = form_curso.save()
                    task1 = form_datos_generales.save(commit=False)
                    #Se realiza la asignación mencionando el formulario de donde vienen las FK
                    task1.id_sobrepeso= task2
                    task1.cp= task3
                    task1.id_curso= task4
                    task1 = form_datos_generales.save()
                    

                    return HttpResponseRedirect('/task')
        
            except ValueError:
                return render(request, 'create_task.html', {
                    'formS': TaskSobrepeso,
                    'formL': TaskLocalidad,
                    'formC': TaskCurso,
                    'form': TaskForm,
                    'error': 'Ingresa información válida'
                })
        case _:
            print('ERROR 404: NOT FOUND')

# Vista de cierre de sesión
@login_required
def singout(request):
    logout(request)
    return redirect('home')

# Vista de inicio de sesión (verifiación)
def singin(request):
    # Si el método es GET se envia al formulario
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    # Si no lo es,significa que se estan eviando datos, se comprueba si los datos son validos
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        # Si el usuario no existe se le avisa al mismo
        if user is None:
            return render(request, 'singin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña son incorrectos'
            })
        # Si existe se envia a la pagina de inicio y se guarda su sesion
        else:
            login(request, user)
            return redirect('home')

# Vista calculadora IMC
@login_required
def calc(request):
    return render(request, 'calc.html')
