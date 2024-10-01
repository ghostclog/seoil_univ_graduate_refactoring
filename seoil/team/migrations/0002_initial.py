# Generated by Django 5.1.1 on 2024-10-01 06:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='chatlog',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teampostcomment',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_post_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teamposts',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teampostcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_post_comment', to='team.teamposts'),
        ),
        migrations.AddField(
            model_name='teams',
            name='members',
            field=models.ManyToManyField(related_name='teams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teams',
            name='team_apply_log',
            field=models.ManyToManyField(related_name='apply_log', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teams',
            name='team_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_masters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teamposts',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_posts', to='team.teams'),
        ),
        migrations.AddField(
            model_name='teampostcomment',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.teams'),
        ),
        migrations.AddField(
            model_name='chatlog',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='team.teams'),
        ),
    ]
