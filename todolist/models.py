from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Status(models.Model):
    value = models.BooleanField(default=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.value


class Task(models.Model):
    description = models.CharField(
            max_length=200,
            help_text='Describe your task',
            validators=[MinLengthValidator(5, "Too short description")]
    )
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.description
