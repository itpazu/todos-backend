# Generated by Django 4.2 on 2023-04-08 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos_api', '0002_alter_todo_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-order', 'created_at']},
        ),
    ]
