from django.urls import path
from .views import todo_list, todo_create, todo_update, todo_delete

app_name = 'todo'

urlpatterns = [
    path('', todo_list, name='list'),
    path('create/', todo_create, name='create'),
    path('update/<int:pk>/', todo_update, name='update'),
    path('delete/<int:pk>/', todo_delete, name='delete'),
]