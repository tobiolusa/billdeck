from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="login"),
    path('register/', views.register, name="register"),
    path('forgot-password/', views.forgot_password, name="forgot_password"),
    path('email-verification/', views.email_verification, name="email-verification"),
]
