from django.urls import path

from . import views

app_name = 'wall'

urlpatterns = [
    path('', views.home, name='home'),

    path('posts/create/', views.create_post, name='create_post'),
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),

    path('comments/create/', views.create_comment, name='create_comment'),

    path(
    'comments/<int:comment_id>/delete/',
    views.delete_comment,
    name='delete_comment',
    ),
]