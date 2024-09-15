from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import UserProfileForm


@login_required
def profile(request):
    User = get_user_model()
    user = User.objects.get(pk=request.user.pk)
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        if "update" in request.POST:
            form = UserProfileForm(request.POST, instance=user)
            profile_form = UserProfileAvatarForm(
                request.POST, request.FILES, instance=user_profile
            )
            if form.is_valid() and profile_form.is_valid():
                form.save()
                profile_form.save()
                return redirect("profile")
        elif "delete" in request.POST:
            user.delete()
            return redirect("home")
    else:
        form = UserProfileForm(instance=user)
        profile_form = UserProfileAvatarForm(instance=user_profile)

    return render(
        request, "accounts/profile.html", {"form": form, "profile_form": profile_form}
    )
