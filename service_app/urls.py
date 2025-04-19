from django.urls import path
from . import views


urlpatterns = [
    path('service_page/',views.service_page,name = 'service_page'),
]