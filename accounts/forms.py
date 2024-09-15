from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class UserProfileAvatarForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar"]
