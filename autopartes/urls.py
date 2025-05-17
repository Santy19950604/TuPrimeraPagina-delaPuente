from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar/marca/', views.agregar_marca, name='agregar_marca'),
    path('agregar/modelo/', views.agregar_modelo, name='agregar_modelo'),
    path('agregar/autoparte/', views.agregar_autoparte, name='agregar_autoparte'),
    path('buscar/', views.buscar_autoparte, name='buscar_autoparte'),
]