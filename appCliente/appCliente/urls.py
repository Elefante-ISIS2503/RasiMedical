from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("ui.urls")),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
]
