from django.urls import path
from django.views.generic import TemplateView
 
urlpatterns = [
    path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html")),
]