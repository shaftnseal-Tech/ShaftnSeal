from django.urls import path
from . import views

urlpatterns = [
    path('', views.maker_model, name='spares_page'),
    path('get_pumpmodels/<int:id>/', views.get_pumpmodels, name='get_pumpmodels'),
    path('get_model_varient/<int:id>/', views.get_model_varient, name='get_model_varient'),
    path('get_parts/<int:model_id>/<int:variant_id>/', views.get_parts, name='get_parts'),
    path('chatbot/', views.spareparts, name='spareparts'),  # chatbot view
]
