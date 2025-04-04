from django.urls import path
from .views import pump_analysis_view

urlpatterns = [
    path('pump-analysis/', pump_analysis_view, name='pump_analysis'),
]
