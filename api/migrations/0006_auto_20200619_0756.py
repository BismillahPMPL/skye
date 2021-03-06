# Generated by Django 3.0.7 on 2020-06-19 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200619_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listener',
            old_name='group_id',
            new_name='creator_id',
        ),
        migrations.RenameField(
            model_name='listener',
            old_name='user_id',
            new_name='listener_id',
        ),
        migrations.AddField(
            model_name='listener',
            name='chat_type',
            field=models.CharField(blank=True, choices=[('USER', 'User'), ('ROOM', 'Room'), ('GROUP', 'Group')], max_length=5),
        ),
        migrations.AddField(
            model_name='listener',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='listener',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='listener',
            name='type',
            field=models.CharField(blank=True, choices=[('FREEGAME', 'Free Game')], max_length=10),
        ),
    ]
