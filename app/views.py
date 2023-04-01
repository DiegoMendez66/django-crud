from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import EmpleadoForm
from .models import Empleado
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registro(request):

    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('empleados')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existente'
                })
        return render(request, 'registro.html', {
                'form': UserCreationForm,
                'error': 'Contraseñas no coinciden'
        })

@login_required
def empleados(request):
    empleados = Empleado.objects.all()

    return render(request, 'empleados.html', {'empleados': empleados})

@login_required
def crear_empleado(request):

    if request.method == 'GET':
        return render(request, 'crear.html', {
            'form': EmpleadoForm
        })
    else:
        try:
            form = EmpleadoForm(request.POST)
            nuevo_emp = form.save(commit=False)
            nuevo_emp.save()
            return redirect('empleados')
        except ValueError:
            return render(request, 'crear.html', {
                'form': EmpleadoForm,
                'error': 'Por favor ingresar datos validos'
            })

@login_required
def empleado_detalle(request, empleado_id):
    if request.method == 'GET':
        empleado = get_object_or_404(Empleado, pk=empleado_id)
        form = EmpleadoForm(instance=empleado)
        return render(request, 'empleado_detalle.html', {'empleado': empleado, 'form': form})
    else:
        try:
            empleado = get_object_or_404(Empleado, pk=empleado_id)
            form = EmpleadoForm(request.POST, instance=empleado)
            form.save()
            return redirect('empleados')
        except ValueError:
            return render(request, 'empleado_detalle.html', {'empleado': empleado, 'form': form, 'error': 'Error al actualizar el empleado'})

@login_required
def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleados')

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
        'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('empleados')
