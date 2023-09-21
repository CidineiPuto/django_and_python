from django.shortcuts import render

from . import data

# Create your views here.


def blog_function_view(request):
    context = {
        "text": "Estamos no blog",
        "posts": data.posts,
    }

    return render(
        request,
        "blog/index.html",
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
