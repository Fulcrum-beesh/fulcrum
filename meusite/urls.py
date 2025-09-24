
from django.urls import path
from meuapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.home, name='home'),
    path('usuarios/',views.usuarios,name='formulario'),
    path('deletar/<int:id_usuario>/', views.deletar_usuario, name='deletar_usuario'),
]