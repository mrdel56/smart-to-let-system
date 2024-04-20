# Generated by Django 5.0.4 on 2024-04-19 10:58

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0007_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]