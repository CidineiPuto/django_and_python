from django.shortcuts import render

# Create your views here.


def blog_function_view(request):
    return render(
        request,
        "blog/index.html",
    )


def exemplo_function_view(request):
    return render(
        request,
        "blog/exemplo.html",
    )
