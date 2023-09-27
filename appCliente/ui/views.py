from django.shortcuts import render


def home(request):
    return render(request, "ui/home.html")


def newDoctor(request):
    return render(request, "ui/newDoctor.html")
