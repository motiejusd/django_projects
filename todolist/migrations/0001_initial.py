# Generated by Django 3.1.3 on 2020-11-07 10:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Describe your task', max_length=200, validators=[django.core.validators.MinLengthValidator(5, 'Too short description')])),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
