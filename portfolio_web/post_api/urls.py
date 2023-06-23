from django.urls import path
from .views import PostListAPIView, PostDetailAPIView

app_name = 'api'

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
]