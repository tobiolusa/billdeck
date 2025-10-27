from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "authapp/login.html")


def register(request):
    return render(request, "authapp/register.html") 

def forgot_password(request):
    return render(request, "authapp/forgot-password.html")
