from django.shortcuts import render, redirect
from .forms import EmpleadoForm
from .models import Empleados
from django.http import JsonResponse


def get_empleados(request):
    empleados = Empleados.objects.all()
    form = EmpleadoForm()
    return render(request, 'empleados.html', {'empleados': empleados, 'form': form})


def guardar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_empleados')
    else:
        form = EmpleadoForm()
        return render(request, 'empleados.html')


def profile_empleado(request):
    return render(request, 'includes/detalleEmpleado.html')
