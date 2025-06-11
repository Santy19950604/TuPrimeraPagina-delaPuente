from django.urls import path
from . import views
from .views import (
    AboutView,
    AutoparteListView,
    AutoparteDetailView,
    AutoparteCreateView,
    AutoparteUpdateView,
    AutoparteDeleteView,
)

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("agregar/marca/", views.agregar_marca, name="agregar_marca"),
    path("agregar/modelo/", views.agregar_modelo, name="agregar_modelo"),
    # path('agregar/autoparte/', views.agregar_autoparte, name='agregar_autoparte'),
    path("buscar/", AutoparteListView.as_view(), name="buscar_autoparte"),
    path("about/", AboutView.as_view(), name="about"),
    path("autopartes/", AutoparteListView.as_view(), name="autoparte_list"),
    path(
        "autopartes/<int:pk>/", AutoparteDetailView.as_view(), name="autoparte_detail"
    ),
    path("autopartes/nueva/", AutoparteCreateView.as_view(), name="autoparte_create"),
    path(
        "autopartes/<int:pk>/editar/",
        AutoparteUpdateView.as_view(),
        name="autoparte_update",
    ),
    path(
        "autopartes/<int:pk>/eliminar/",
        AutoparteDeleteView.as_view(),
        name="autoparte_delete",
    ),
]
