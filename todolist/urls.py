from django.urls import path
from todolist.views import register, login_user, logout_user, update, delete
from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task', views.create_task, name='create task'),
    path('update/<int:id>', update, name = 'update'),
    path('delete/<int:id>', delete, name = 'delete'),
]