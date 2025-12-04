from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('add/<int:component_id>/', views.add_to_basket, name='add_to_basket'),
    path('view/', views.view_basket, name='view_basket'),
]
