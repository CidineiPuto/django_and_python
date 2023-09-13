from django.urls import path

from . import views  # . = blog

urlpatterns = [
    path("", views.blog_function_view),
    path("exemplo/", views.exemplo_function_view),
]
