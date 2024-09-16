from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import (
    UserChangeForm as BaseUserChangeForm,
    PasswordChangeForm as BasePasswordChangeForm,
)
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar"]  # Ajusta según los campos que quieras editar


class UserProfileAvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar"]  # Ajusta según los campos necesarios


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ["username"]  # Ajusta según los campos que quieras editar


class PasswordChangeForm(BasePasswordChangeForm):
    class Meta:
        model = User
        fields = [
            "old_password",
            "new_password1",
            "new_password2",
        ]  # Incluye todos los campos necesarios
