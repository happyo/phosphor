# Generated by Django 2.2 on 2019-04-23 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190423_0801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertodo',
            old_name='todo',
            new_name='todo_id',
        ),
    ]
