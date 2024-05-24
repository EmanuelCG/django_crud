from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmpleadoForm
from .models import Empleados
from django.urls import reverse
from django.contrib import messages


def get_empleados(request):
    empleados = Empleados.objects.all()
    form = EmpleadoForm()
    return render(request, 'empleados.html', {'empleados': empleados, 'form': form})


def guardar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'El empleado se creo con éxito.')
            return redirect('get_empleados')
    else:
        form = EmpleadoForm()
        return render(request, 'empleados.html')


def profile_empleado(request, empleado_id):

    empleado = get_object_or_404(Empleados, pk=empleado_id)
    form = EmpleadoForm(instance=empleado)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'El empleado se actualizó con éxito.')
            return redirect(reverse('profile_empleado', kwargs={'empleado_id': empleado_id}))
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'includes/detalleEmpleado.html', {'empleado': empleado, 'form': form})


def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleados, pk=empleado_id)
    if request.method == "POST":
        empleado.delete()
        messages.success(
            request, 'El empleado ha sido eliminado exitosamente.')
        return redirect('get_empleados')
    else:
        return render(request, 'empleados.html')
