# Generated by Django 3.0.7 on 2020-06-18 22:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('original_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('discount', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('USER', 'user'), ('ROOM', 'room'), ('GROUP', 'group')], max_length=5)),
            ],
        ),
    ]
