from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
]
