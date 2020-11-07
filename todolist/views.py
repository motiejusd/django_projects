from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from todolist.models import Task
from todolist.forms import MakeForm
# from django.http import HttpResponse
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    success_url = reverse_lazy('todolist:index')
    form = MakeForm()

    if request.method == 'POST':
        form = MakeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(success_url)

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todolist/main.html', context)
