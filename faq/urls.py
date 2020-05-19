from django.urls import path
from .views import frequently_asked_view

urlpatterns = [
    path("", frequently_asked_view, name="frequently_asked")
]
