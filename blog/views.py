from typing import Any

from django.http import Http404, HttpRequest
from django.shortcuts import render

from . import data

# Create your views here.


def blog_function_view(request):
    context = {
        "posts": data.posts,
    }

    return render(
        request,
        "blog/index.html",
        context,
    )


def post_function_view(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in data.posts:
        if post["id"] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404("Post não existe.")

    context = {
        "post": found_post,
        "title": found_post["title"] + " - ",
    }

    return render(
        request,
        "blog/post.html",
        context,
    )


def exemplo_function_view(request):
    context = {
        "text": "Estamos no exemplo",
        "title": "Essa é uma página de exemplo - ",
    }

    return render(
        request,
        "blog/exemplo.html",
        context,
    )
