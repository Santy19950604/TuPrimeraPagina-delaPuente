from django.shortcuts import render
from .forms import MarcaForm, ModeloForm, BuscarAutoparteForm
from .models import Autoparte
from django.db.models import Q
from django.contrib import messages
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def inicio(request):
    return render(request, "autopartes/index.html")


def agregar_marca(request):
    form = MarcaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Marca agregada exitosamente.")
            form = MarcaForm()
    return render(
        request, "autopartes/formulario.html", {"form": form, "titulo": "Agregar Marca"}
    )


def agregar_modelo(request):
    form = ModeloForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Modelo agregado exitosamente.")
            form = ModeloForm()
    return render(
        request,
        "autopartes/formulario.html",
        {"form": form, "titulo": "Agregar Modelo"},
    )


# def agregar_autoparte(request):
#    form = AutoparteForm(request.POST or None, request.FILES or None)
#    if request.method == 'POST':
#        if form.is_valid():
#            form.save()
#            messages.success(request, "Autoparte agregada exitosamente.")
#            form = AutoparteForm()
#    return render(request, 'autopartes/formulario.html', {'form': form, 'titulo': 'Agregar Autoparte'})
#


def buscar_autoparte(request):
    resultados = []
    mensaje = ""
    form = BuscarAutoparteForm(request.GET or None)

    if form.is_valid():
        criterio = form.cleaned_data["criterio"]
        if criterio:
            resultados = Autoparte.objects.filter(
                Q(marca__nombre__icontains=criterio)
                | Q(modelo__nombre__icontains=criterio)
                | Q(descripcion__icontains=criterio)
                | Q(numero_serie__icontains=criterio)
            ).select_related("marca", "modelo")

        if not resultados:
            mensaje = "No se encontraron autopartes con ese criterio."

    return render(
        request,
        "autopartes/buscar.html",
        {"form": form, "resultados": resultados, "mensaje": mensaje},
    )


class AboutView(TemplateView):
    template_name = "about.html"


class AutoparteListView(ListView):
    model = Autoparte
    template_name = "autopartes/autoparte_list.html"
    context_object_name = "autopartes"

    def get_queryset(self):
        queryset = super().get_queryset().select_related("marca", "modelo")
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(numero_serie__icontains=q)
                | Q(descripcion__icontains=q)
                | Q(marca__nombre__icontains=q)
                | Q(modelo__nombre__icontains=q)
            )
        return queryset


class AutoparteDetailView(DetailView):
    model = Autoparte
    template_name = "autopartes/autoparte_detail.html"
    context_object_name = "autoparte"


class AutoparteCreateView(LoginRequiredMixin, CreateView):
    model = Autoparte
    fields = ["numero_serie", "descripcion", "imagen", "marca", "modelo"]
    template_name = "autopartes/formulario.html"
    success_url = reverse_lazy("autoparte_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Autoparte agregada exitosamente.")
        return response


class AutoparteUpdateView(LoginRequiredMixin, UpdateView):
    model = Autoparte
    fields = ["numero_serie", "descripcion", "imagen", "marca", "modelo"]
    template_name = "autopartes/formulario.html"
    success_url = reverse_lazy("autoparte_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Autoparte actualizada exitosamente.")
        return response


class AutoparteDeleteView(LoginRequiredMixin, DeleteView):
    model = Autoparte
    template_name = "autopartes/autoparte_confirm_delete.html"
    success_url = reverse_lazy("autoparte_list")
