"""
URL configuration for petstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path("signup/", views.signup, name='signup'),
    path("logout/", views.handlelogout, name='handlelogout'),
    path("login/", views.handlelogin, name='handlelogin'),
    path("baseauthhh/", views.baseauthh, name='baseauthh'),
    path("actiavte/<uidb64>/<token>",views.ActivateAccountView.as_view(),name="activate"),
    #path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    #path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),
]
