from django.shortcuts import render

# Create your views here.


def home_function_view(request):
    context = {"text": "Estamos na home"}
    return render(
        request,
        "home/index.html",
        context,
    )
