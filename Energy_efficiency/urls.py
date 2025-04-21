from django.urls import path
from . import views

urlpatterns = [
    path('form-page/', views.boiler_form, name='form-page'),
    path('',views.Energy_efficiency_view, name='Energy_efficiency_home'),
    path('boiler-feedpump/',views.boiler_feedpump_view, name='boiler_feedpump'),
    path('boiler-1r+1s-feedpump/',views.boiler_feedpump_1r1s_view, name='boiler_feedpump_1r+1s'),
    path('boiler-2r+1s-feedpump/',views.boiler_feedpump_2r1s_view, name='boiler_feedpump_2r+1s'),
    path('final_submission/',views.finalize_submission, name='final_submission'),
    path('Efficiency_calculater/',views.pump_efficiency_calculater, name='Efficiency_calculater'),

]
