# from django.contrib import admin
from django.urls import path,include
from todo import views

urlpatterns = [
    path('', views.index,name='index'),
    path('task/', views.task,name='task'),
    path("delete_todo/<int:todo_id>/", views.delete_todo, name='delete_todo'),
    path("update/<int:pk>/", views.update_task, name="update_task"),
    path("delete_all/", views.delete_all, name="delete_all"),
    path("logout/", views.LogoutView, name="logout"),
    
]
