# Generated by Django 4.2.5 on 2023-11-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_alter_task_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="ordering",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="todo",
            name="ordering",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
