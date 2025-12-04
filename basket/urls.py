from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
     path('add/<int:component_id>/', views.add_to_basket, name='add_to_basket'),
     path('view/', views.view_basket, name='view_basket'),
     path('update/<int:component_id>/', 
          views.update_basket, name='update_basket'),
     path('remove/<int:component_id>/', 
          views.remove_from_basket, name='remove_from_basket'),
]
