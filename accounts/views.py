from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import sweetify
from .forms import UserRegisterForm


@login_required
def logout(request):
    """Log the user out."""
    auth.logout(request)
    sweetify.success(
        request,
        "You have been successfully logged out."
    )
    return redirect(reverse("home"))


def registration(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                "Account created successfully."
            )
            user = auth.authenticate(request, username=form.cleaned_data.get("username"),
                                     password=form.cleaned_data.get("password1"))
            if user is not None:
                auth.login(request, user)
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form, "page_title": "Register | PrintCrate"})
