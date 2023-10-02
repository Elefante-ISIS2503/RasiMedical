from django.urls import path
from . import views

urlpatterns = [
    path("submitInventario", views.submitInventario, name="submitInventario"),
    path("getInventario", views.getInventario, name="getInventario"),
    path("health-check/", views.healthCheck),
]
