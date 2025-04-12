from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]