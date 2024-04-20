# Generated by Django 5.0.3 on 2024-04-20 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_no', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('rooms', models.IntegerField()),
                ('washrooms', models.IntegerField()),
                ('kitchen', models.IntegerField()),
                ('balcony', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('property_img', models.ImageField(null=True, upload_to='property/')),
                ('visibility', models.BooleanField(default=True)),
                ('price', models.FloatField(default=0.0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.location')),
            ],
        ),
    ]
