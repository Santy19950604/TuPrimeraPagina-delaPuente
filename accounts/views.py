from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. Bienvenido!")
            return redirect('inicio')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        password_form = PasswordChangeForm(request.user, request.POST) if request.POST.get('old_password') else None

        if user_form.is_valid() and profile_form.is_valid():
            if password_form:
                if password_form.is_valid():
                    user_form.save()
                    profile_form.save()
                    user = password_form.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, "Perfil y contraseña actualizados correctamente.")
                    return redirect('profile')
                else:
                    messages.error(request, "Error en el formulario de contraseña.")
            else:
                user_form.save()
                profile_form.save()
                messages.success(request, "Perfil actualizado correctamente.")
                return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'accounts/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form,
    })

# Create your views here.
