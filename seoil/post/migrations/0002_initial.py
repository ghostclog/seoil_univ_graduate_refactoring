# Generated by Django 5.1.1 on 2024-09-29 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='team_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='team.team'),
        ),
    ]