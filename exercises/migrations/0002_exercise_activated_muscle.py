# Generated by Django 5.0.1 on 2024-02-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
        ('muscle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='activated_muscle',
            field=models.ManyToManyField(related_name='muscle', to='muscle.activatedmuscle'),
        ),
    ]
