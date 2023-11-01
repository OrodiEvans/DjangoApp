from django.contrib import admin
from django.urls import path
from EvansApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('sample/', views.sample, name='sample'),
    path('gallery/', views.gallery, name='gallery'),
    path('gal', views.gal, name='gallery-single'),
]
