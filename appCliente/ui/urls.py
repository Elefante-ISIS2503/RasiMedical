from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("newDoctor", views.newDoctor, name="newDoctor"),
    path("submitDoctor", views.submitDoctor, name="submitDoctor"),
    path("showDoctors", views.showDoctors, name="showDoctors"),
]
