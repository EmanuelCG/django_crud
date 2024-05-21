from django.urls import path
from . import views
urlpatterns = [
    path('', views.mostrar_empleados, name="mostrar_empleados"),
    path('', views.nuevo_empleado, name="nuevo_empleado")
]
