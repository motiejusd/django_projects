from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Task(models.Model):
    description = models.CharField(
            max_length=200,
            help_text='Describe your task',
            validators=[MinLengthValidator(5, "Too short description")]
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.description
