from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('empleados/', views.empleados, name='empleados'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('empleados/<int:empleado_id>/', views.empleado_detalle, name='empleado_detalle'),
    path('empleados/<int:empleado_id>/eliminar', views.eliminar_empleado, name='eliminar_empleado'),          
    path('logout/', views.cerrar_sesion, name='logout'),
    path('login/', views.iniciar_sesion, name='login'),
]
