from django.contrib import admin
from django.urls import path
from petapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('copy/', views.copy, name= 'copy'),
    path('checkout/', views.checkout, name="Checkout"),
]

