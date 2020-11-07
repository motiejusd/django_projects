from django.shortcuts import render
from django.views import View

from todolist.models import Task

# from django.http import HttpResponse
# Create your views here.


class MainView(View):
    def get(self, request):
        task_count = Task.objects.all().count()
        tasks = Task.objects.all()
        context = {'task_count': task_count, 'tasks': tasks}
        return render(request, 'todolist/main.html', context)
