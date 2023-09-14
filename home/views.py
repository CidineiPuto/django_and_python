from django.shortcuts import render

# Create your views here.


def home_function_view(request):
    return render(
        request,
        "home/index.html",
    )
