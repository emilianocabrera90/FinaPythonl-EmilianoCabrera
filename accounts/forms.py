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
        fields = ["avatar"] 


class UserProfileAvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar"]  


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ["username"]  


class CustomPasswordChangeForm(BasePasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Old Password"}
        )
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "New Password"}
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm New Password"}
        )
    )
