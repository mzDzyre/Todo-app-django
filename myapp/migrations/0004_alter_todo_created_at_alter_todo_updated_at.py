# Generated by Django 5.0.4 on 2024-04-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_todo_created_at_alter_todo_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
