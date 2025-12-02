from django.urls import path 
from . import views

urlpatterns = [
    path('', views.ComponentList.as_view(), name='home'),
    path('component/<slug:slug>/', 
         views.component_detail, name='component_detail'),
    path('component/<slug:slug>/edit_comment/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
    path('component/<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),    
]
