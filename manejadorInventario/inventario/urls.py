from django.urls import path
from . import views

urlpatterns = [
    path("saveInventario", views.saveInventario, name="saveInventario"),
    path("postInventarios", views.postInventarios, name="postInventarios"),
    path("searchInventario", views.searchInventario, name="searchInventario"),
    path("health-check/", views.healthCheck),
]
