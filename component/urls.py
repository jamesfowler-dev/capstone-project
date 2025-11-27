from django.urls import path 
from . import views

urlpatterns = [
    path('', views.ComponentList.as_view(), name='home'),
    path('<slug:slug>/', views.component_detail, name='component_detail'),
]
