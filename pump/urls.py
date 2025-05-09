from django.urls import path
from . import views


urlpatterns = [
    path('pump/',views.pump_page,name = 'pump'),
    path('error_page/',views.error_page,name = 'error_page'),
]