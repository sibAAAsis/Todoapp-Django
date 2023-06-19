#this is the url patterns of the app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('signup/', views.signup, name='signup'), 
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('account/', views.account, name='account'),
    path('tasks/<int:task_id>/update/', views.update_task, name='update_task'),

]
