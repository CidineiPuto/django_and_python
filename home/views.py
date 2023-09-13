from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_function_view(request):
    locale_ = "Home do app"
    return HttpResponse(f"Uma mensagem vindo da/o {locale_}.")
