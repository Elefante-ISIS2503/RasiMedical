from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Adds urls from profesionales app
    path("", include("profesionales.urls")),
    path('health-check/', views.healthCheck),
]
