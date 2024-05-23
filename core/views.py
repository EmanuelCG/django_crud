from django.shortcuts import render
from empleados.models import Empleados
from empleados.forms import EmpleadoForm


def home(request):
    empleados = Empleados.objects.all()
    form = EmpleadoForm()
    return render(request, 'home.html')
