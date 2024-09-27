from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from accounts.models import UserProfile
from django.contrib.auth import logout


@login_required
def home(request):
    posts = Post.objects.all()
    user_profile = UserProfile.objects.get(user=request.user)
    return render(
        request, "blog/home.html", {"posts": posts, "user_profile": user_profile}
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/update_post.html", {"form": form, "post": post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if post.author == request.user or request.user.is_superuser:
            post.delete()
            return redirect("home")
        else:
            return render(
                request,
                "blog/delete_post.html",
                {"post": post, "error": "No tienes permiso para eliminar este post."},
            )
    return render(request, "blog/delete_post.html", {"post": post})


def logout_view(request):
    logout(request)
    return redirect("home")
