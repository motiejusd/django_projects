from django.forms import ModelForm
from todolist.models import Task
from django import forms


class MakeForm(ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Add task here',
            }
        )
    )

    class Meta:
        model = Task
        fields = '__all__'
