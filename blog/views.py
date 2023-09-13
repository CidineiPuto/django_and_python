from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def blog_function_view(request):
    locale_ = "blog do app 1"
    return HttpResponse(f"Uma mensagem vindo da/o {locale_}.")


def exemplo_function_view(request):
    locale_ = "exemplo do app 1"
    return HttpResponse(f"Uma mensagem vindo da/o {locale_}.")
