from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import sweetify
from .forms import UserRegisterForm, UserCredentialsUpdateForm
from checkout.models import OrderDetail, CustomerShipping
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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


def profile(request):
    user = User.objects.get(username=request.user)
    print(f"====\n {user.id} \n====")
    user_orders = OrderDetail.objects.filter(
        shipping__customer_id=user.id)
    if request.method == "POST":
        form = UserCredentialsUpdateForm(request.POST, instance=user)
        if form.is_valid():
            new_credentials = form.save(commit=False)
            hashed_password = make_password(form.cleaned_data["password"])
            new_credentials.password = hashed_password
            new_credentials.save()
            return redirect("home")
    else:
        form = UserCredentialsUpdateForm(instance=user)
    return render(request, "profile.html", {"page_title": "Profile | PrintCrate", "user_orders": user_orders, "form": form})
