# Generated by Django 5.0.3 on 2024-03-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Is employee'),
        ),
    ]
