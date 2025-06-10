from django.urls import path
from . import views

urlpatterns = [
    path('', views.bandeja_entrada, name='bandeja'),
    path('enviar/<int:receptor_id>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('seleccionar/', views.seleccionar_destinatario, name='seleccionar_destinatario'),
    path('enviar/<int:receptor_id>/', views.enviar_mensaje, name='enviar_mensaje'),
]