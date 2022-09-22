from django.urls import URLPattern, path
from .views import post_detail, render_posts

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name="posts"),
    path('<int:post_id>', post_detail, name="post_detail"),
]