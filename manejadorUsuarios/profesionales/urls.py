from django.urls import path
from . import views

urlpatterns = [
    path("saveDoctor", views.saveDoctor, name="saveDoctor"),
    path("postDoctors", views.postDoctors, name="postDoctors"),
    path("postAllDoctors", views.postAllDoctors, name="postAllDoctors"),
    path("health-check/", views.healthCheck),
]
