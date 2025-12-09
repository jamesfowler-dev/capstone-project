from django.urls import path 
from . import views

urlpatterns = [
    path(
        '', 
        views.ComponentList.as_view(),
        name='home',
    ),
    path('component/<slug:slug>/', 
        views.component_detail, name='component_detail'),
    path('component/<slug:slug>/edit_review/<int:review_id>/',
        views.review_edit, name='review_edit'),
    path('component/<slug:slug>/delete_review/<int:review_id>/',
        views.review_delete, name='review_delete'),
    path('component/<slug:slug>/edit_comment/<int:comment_id>/',
        views.comment_edit, name='comment_edit'),
    path('component/<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),    
    path('search/', views.component_search, name='component_search'),
]
