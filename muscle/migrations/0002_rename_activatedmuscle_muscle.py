# Generated by Django 5.0.1 on 2024-02-06 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0002_exercise_activated_muscle"),
        ("muscle", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ActivatedMuscle",
            new_name="Muscle",
        ),
    ]
