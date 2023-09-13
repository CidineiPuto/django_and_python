from django.urls import path

from . import views  # . = home

urlpatterns = [
    path("", views.home_function_view),
]
