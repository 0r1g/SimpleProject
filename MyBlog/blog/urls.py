from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:post_id>/', views.get_post, name='post'),
    path('author/<int:author_id>/', views.get_posts_by_author, name='author')
]
