from django.urls import path
from . import views

urlpatterns = [
    path('', views.maker_model, name='spares_page'),
    path('get_pumpmodels/<uuid:id>/', views.get_pumpmodels, name='get_pumpmodels'),
    path('get_model_varient/<uuid:id>/', views.get_model_varient, name='get_model_varient'),
    path('get_model_design/<uuid:id>/', views.get_model_design, name='get_model_design'),
    path('get_parts/<uuid:model_id>/<uuid:variant_id>/<uuid:design_id>', views.get_parts, name='get_parts'),
]
