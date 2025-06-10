from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User

@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(receptor=request.user).order_by('-fecha_envio')
    return render(request, 'mensajeria/bandeja_entrada.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request, receptor_id):
    receptor = get_object_or_404(User, pk=receptor_id)
    
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            contenido = form.cleaned_data['contenido']
            mensaje = Mensaje.objects.create(
                emisor=request.user,
                receptor=receptor,
                contenido=contenido,
                leido=False
            )
            return redirect('bandeja')  # O la vista que muestre los mensajes recibidos
    else:
        form = MensajeForm()
        
    return render(request, 'mensajeria/enviar_mensaje.html', {'form': form, 'receptor': receptor})

@login_required
def seleccionar_destinatario(request):
    usuarios = User.objects.exclude(id=request.user.id)
    return render(request, 'mensajeria/seleccionar_destinatario.html', {'usuarios': usuarios})

# Create your views here.
