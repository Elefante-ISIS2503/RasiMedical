from django.urls import path
from . import views

urlpatterns = [
    path("submitDoctor", views.submitDoctor, name="submitDoctor"),
    path("getDoctors", views.getDoctors, name="getDoctors"),
    path('health-check/', views.healthCheck),
]
