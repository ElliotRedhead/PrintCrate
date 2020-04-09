from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import registration, logout

urlpatterns = [
    path("logout", logout, name="logout"),
    path("register", registration, name="register"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
