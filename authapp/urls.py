from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="login"),
    path('register/', views.register, name="register"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
]
