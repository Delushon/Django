from django.http import *
from django.shortcuts import render
from django.contrib import admin
from firstapp import views
from django.template.response import TemplateResponse
from .forms import UserForm
from django.http import HttpResponseRedirect
from .models import Person

# получение данных из бд


def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})

# сохранение данных в бд


def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")


def about(request):
    return render(request, "firstapp/home.html")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


def m304(request):
    return HttpResponseNotModified()


def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")


def m403(request):
    return HttpResponseForbidden("<h2>Forbidden</h2>")


def m404(request):
    return HttpResponseNotFound("<h2>Not Found</h2>")


def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")


def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")
