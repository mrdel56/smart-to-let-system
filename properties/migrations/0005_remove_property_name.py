# Generated by Django 5.0.2 on 2024-04-21 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='name',
        ),
    ]
