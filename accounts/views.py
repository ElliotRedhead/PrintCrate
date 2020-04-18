from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


@login_required
def logout(request):
    """Log the user out."""
    auth.logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect(reverse("home"))


def registration(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form, "page_title": "Register | PrintCrate"})
