from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("newDoctor", views.newDoctor, name="newDoctor"),
    path("newInventario", views.newInventario, name="newInventario"),
    path("submitDoctor", views.submitDoctor, name="submitDoctor"),
    path(
        "InventarioSearchFront",
        views.InventarioSearchFront,
        name="InventarioSearchFront",
    ),
    path("getDoctors", views.getDoctors, name="getDoctors"),
    path("submitInventario", views.submitInventario, name="submitInventario"),
    path("getInventario", views.getInventario, name="getInventario"),
]
