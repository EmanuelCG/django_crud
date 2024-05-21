from django.shortcuts import render, redirect
from .forms import EmpleadoForm
from .models import Empleados
# Create your views here.


def mostrar_empleados(request):
    empleados = Empleados.objects.all()
    form = EmpleadoForm()
    return render(request, 'home.html', {'empleados': empleados, 'form': form})


def nuevo_empleado(request):
    context = {}
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                pass
    else:
        context['form'] = EmpleadoForm()
    return render(request, 'home.html', context)
