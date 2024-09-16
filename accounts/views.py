from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import (
    UserProfileForm,
    UserProfileAvatarForm,
    UserChangeForm,
    CustomPasswordChangeForm,
)
from .models import UserProfile


@login_required
def profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        if "update_profile" in request.POST:
            profile_form = UserProfileAvatarForm(
                request.POST, request.FILES, instance=user_profile
            )
            if profile_form.is_valid():
                profile_form.save()
                return redirect("profile")
        elif "change_password" in request.POST:
            password_form = CustomPasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect("profile")
        elif "delete" in request.POST:
            user.delete()
            return redirect("home")
    else:
        profile_form = UserProfileAvatarForm(instance=user_profile)
        password_form = CustomPasswordChangeForm(user)

    return render(
        request,
        "accounts/profile.html",
        {"profile_form": profile_form, "password_form": password_form},
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
