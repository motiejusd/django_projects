from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Count
# from . import View

from todolist.models import Task
from todolist.forms import MakeForm
# from django.http import HttpResponse
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    tasks_count = tasks.count()
    success_url = reverse_lazy('todolist:index')  # resolve Django URL name to URL path
    form = MakeForm()

    if request.method == 'POST':
        form = MakeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(success_url)

    filter = request.GET.get('filter', False)
    if filter == 'completed':
        tasks = Task.objects.filter(status=True)
    elif filter == 'not_completed':
        tasks = Task.objects.filter(status=False)
    else:
        filter = False

    context = {'tasks': tasks, 'form': form, 'tasks_count': tasks_count}
    return render(request, 'todolist/main.html', context)


def update(request, pk):
    task = get_object_or_404(Task, id=pk)
    form = MakeForm(instance=task)
    success_url = reverse_lazy('todolist:index')

    if request.method == 'POST':
        form = MakeForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect(success_url)

    context = {'form': form}
    return render(request, 'todolist/update.html', context)


def delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    success_url = reverse_lazy('todolist:index')

    if request.method == 'POST':
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return redirect(success_url)
    context = {'task': task}
    return render(request, 'todolist/delete.html', context)
