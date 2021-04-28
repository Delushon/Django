from django.urls import path
from django.views.generic import TemplateView
from firstapp import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
]
