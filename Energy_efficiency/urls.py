from django.urls import path
from . import views

urlpatterns = [
    path('pump-analysis/', views.pump_analysis_view, name='pump_analysis'),
    path('',views.Energy_efficiency_view, name='Energy_efficiency_home'),
    path('boiler-feedpump/',views.boiler_feedpump_view, name='boiler_feedpump'),
    path('boiler-1r+1s-feedpump/',views.boiler_feedpump_1r1s_view, name='boiler_feedpump_1r+1s'),

]
