from django.urls import path
from . import views

urlpatterns = [
    path("saveDoctor", views.saveDoctor, name="saveDoctor"),
    path("postDoctors", views.postDoctors, name="postDoctors"),
    path("health-check/", views.healthCheck),
]
