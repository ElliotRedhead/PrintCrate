"""printcrate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts import urls as accounts_urls
from about import urls as about_urls
from homepage import urls as homepage_urls
from products import urls as products_urls
from cart import urls as cart_urls
from checkout import urls as checkout_urls

urlpatterns = [
    path("", include(homepage_urls)),
    path("admin/", admin.site.urls),
    path("about/", include(about_urls)),
    path("accounts/", include(accounts_urls)),
    path("products/", include(products_urls)),
    path("cart/", include(cart_urls)),
    path("checkout/", include(checkout_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
