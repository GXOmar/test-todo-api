# Generated by Django 5.0.6 on 2024-05-20 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_todo_tag'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='todo',
            unique_together={('title', 'description')},
        ),
    ]
