from django.urls import path
from django.views.generic import TemplateView
from firstapp import views
 
urlpatterns = [
    path('about/', TemplateView.as_view(template_name="firstapp/about.html", 
        extra_context={"header": "О сайте"})),
    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html")),
    path('', views.index),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete)
]