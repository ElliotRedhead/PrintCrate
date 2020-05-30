from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import sweetify
from checkout.models import OrderDetail
from .forms import UserRegisterForm, UserCredentialsUpdateForm


@login_required
def logout(request):
    """Log the user out."""
    auth.logout(request)
    sweetify.success(
        request,
        title="You have been successfully logged out.",
        icon="success"
    )
    return redirect(reverse("home"))


def registration(request):
    """Handle user registration and success feedback.

    Redirects to account profile details if user is authenticated.
    If user has been redirected to register e.g. due to checkout in progress
    they are redirected to previous page following successful registration.
    User is authenticated following successful registration with success modal.
    """

    if request.user.is_authenticated:
        return redirect("profile")
    previous_page = request.META.get("HTTP_REFERER")
    form = UserRegisterForm(request.POST)
    if previous_page:
        if "next" in previous_page:
            marker_index = previous_page.index("next")
            string_length = len(previous_page)
            redirect_string = previous_page[marker_index+5:string_length]
            request.session["redirect_target"] = redirect_string
    if request.method == "POST":
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                title="Account created successfully.",
                icon="success"
            )
            user = auth.authenticate(
                request,
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password1")
            )
            if user is not None:
                auth.login(request, user)
                if request.session.get("redirect_target"):
                    return HttpResponseRedirect(
                        request.session["redirect_target"]
                    )
                return redirect("profile")
    else:
        form = UserRegisterForm()
    return render(
        request,
        "register.html",
        {"form": form, "page_title": "Register | PrintCrate"}
    )


@login_required
def profile(request):
    """Create account profile page with update credentials form.

    Serves as default page to redirect following login, sweetalert modal integrated.
    Orders are filtered to display logged in user's orders only.
    A validated user update form enables user to update their credentials,
    a success modal is displayed on update success.
    """
    previous_page = request.META.get("HTTP_REFERER")
    if previous_page:
        if previous_page.endswith("login"):
            sweetify.success(
                request,
                title="Login successful.",
                icon="success",
            )
    user = User.objects.get(username=request.user)
    user_orders = OrderDetail.objects.filter(
        shipping__customer_id=user.id)
    if request.method == "POST":
        form = UserCredentialsUpdateForm(request.POST, instance=user)
        if form.is_valid():
            new_credentials = form.save(commit=False)
            hashed_password = make_password(form.cleaned_data["password"])
            new_credentials.password = hashed_password
            new_credentials.save()
            sweetify.success(
                request,
                "Your credentials have been updated, please login."
            )
            return redirect("login")
    else:
        form = UserCredentialsUpdateForm(instance=user)
    return render(request, "profile.html", {"page_title": "Profile | PrintCrate", "user_orders": user_orders, "form": form})
