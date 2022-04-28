from django.urls import path
from techboxapp import views

urlpatterns = [
    path('', views.home),
    path('base', views.base)
]