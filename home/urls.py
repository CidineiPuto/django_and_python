from django.urls import path

from . import views  # . = home

app_name = "home"

urlpatterns = [
    path("", views.home_function_view, name="home"),
]
