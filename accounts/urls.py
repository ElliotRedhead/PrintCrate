from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth
from django.urls import path

from .views import logout, profile, registration

urlpatterns = [
    path("logout", logout, name="logout"),
    path("register", registration, name="register"),
    path(
        "login",
        auth.LoginView.as_view(
            template_name="login.html",
            redirect_authenticated_user=True,
            extra_context={"page_title": "Login | PrintCrate"},
        ),
        name="login",
    ),
    path("profile", profile, name="profile"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
