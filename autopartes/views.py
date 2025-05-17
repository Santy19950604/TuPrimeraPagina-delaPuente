from django.shortcuts import render, redirect
from .forms import MarcaForm, ModeloForm, AutoparteForm, BuscarAutoparteForm
from .models import Autoparte
from django.db.models import Q

def inicio(request):
    return render(request, 'autopartes/index.html')

def agregar_marca(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'autopartes/formulario.html', {'form': form, 'titulo': 'Agregar Marca'})

def agregar_modelo(request):
    form = ModeloForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'autopartes/formulario.html', {'form': form, 'titulo': 'Agregar Modelo'})

def agregar_autoparte(request):
    form = AutoparteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'autopartes/formulario.html', {'form': form, 'titulo': 'Agregar Autoparte'})

def buscar_autoparte(request):
    resultados = []
    mensaje = ''
    form = BuscarAutoparteForm(request.GET or None)

    if form.is_valid():
        criterio = form.cleaned_data['criterio']
        if criterio:
            resultados = Autoparte.objects.filter(
                Q(marca__nombre__icontains=criterio) |
                Q(modelo__nombre__icontains=criterio) |
                Q(descripcion__icontains=criterio) |
                Q(numero_serie__icontains=criterio)
            ).select_related('marca', 'modelo')

        if not resultados:
            mensaje = "No se encontraron autopartes con ese criterio."

    return render(request, 'autopartes/buscar.html', {
        'form': form,
        'resultados': resultados,
        'mensaje': mensaje
    })
