from django.urls import path

from . import views  # . = blog

app_name = "blog"

# blog/
urlpatterns = [
    path("", views.blog_function_view, name="home"),
    path("post/<int:id>", views.post_function_view, name="post"),
    path("exemplo/", views.exemplo_function_view, name="exemplo"),
]
