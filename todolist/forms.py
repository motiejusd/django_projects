from django.forms import ModelForm
from todolist.models import Task


class MakeForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
