# Generated by Django 3.0.7 on 2020-06-18 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200619_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listener',
            name='group_id',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='listener',
            name='user_id',
            field=models.CharField(max_length=150),
        ),
    ]
