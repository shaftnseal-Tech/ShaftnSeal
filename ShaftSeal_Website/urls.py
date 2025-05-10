"""
URL configuration for ShaftSeal_Website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os
from django.conf import settings
from django.conf.urls.static import static
from ShaftSeal_Website.settings import BASE_DIR  # Adjust if your settings.py path differs

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('Spares/', include('Spares.urls')),
    path('', include('Products.urls')),
    path("Energy_efficiency/", include("Energy_efficiency.urls")),
    path('service_app/', include('service_app.urls')),
    path('pump/', include('pump.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(BASE_DIR, 'static'))

