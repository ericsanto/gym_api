# Generated by Django 5.0.1 on 2024-02-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exercises", "0002_exercise_activated_muscle"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercise",
            name="execution",
            field=models.URLField(blank=True, null=True),
        ),
    ]
