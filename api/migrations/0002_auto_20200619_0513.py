# Generated by Django 3.0.7 on 2020-06-18 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listener',
            name='group_id',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='listener',
            name='user_id',
            field=models.CharField(default='', max_length=150),
        ),
    ]
