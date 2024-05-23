from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_empleados, name="get_empleados"),
    path('create/', views.guardar_empleado, name="create_empleado"),
    path('profile/', views.profile_empleado, name="profile_empleado")
]
