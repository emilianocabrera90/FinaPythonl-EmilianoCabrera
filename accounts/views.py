from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import UserProfileForm, UserProfileAvatarForm, UserChangeForm
from .models import UserProfile


@login_required
def profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        if "update_profile" in request.POST:
            # Formulario para actualizar el perfil de usuario
            form = UserChangeForm(request.POST, instance=user)
            profile_form = UserProfileAvatarForm(
                request.POST, request.FILES, instance=user_profile
            )
            if form.is_valid() and profile_form.is_valid():
                form.save()
                profile_form.save()
                return redirect("profile")
        elif "change_password" in request.POST:
            # Formulario para cambiar la contraseña
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                password_form.save()
                # Re-autenticamos al usuario para que use la nueva contraseña
                login(request, user)
                return redirect("profile")
        elif "delete" in request.POST:
            user.delete()
            return redirect("home")
    else:
        form = UserChangeForm(instance=user)
        profile_form = UserProfileAvatarForm(instance=user_profile)
        password_form = PasswordChangeForm(user)

    return render(
        request,
        "accounts/profile.html",
        {"form": form, "profile_form": profile_form, "password_form": password_form},
    )


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")
