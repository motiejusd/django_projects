from django.urls import path, include
from todolist import views

app_name = 'todolist'
urlpatterns = [
    path('', views.home, name='home'),
]
