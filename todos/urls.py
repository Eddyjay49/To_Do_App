from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:id>/', views.task_detail, name='task_detail'),
    path('task/add/', views.task_create, name='task_create'),
    path('task/edit/<int:id>/', views.task_edit, name='task_edit'),
    path('task/delete/<int:id>/', views.task_delete, name='task_delete'),
]
