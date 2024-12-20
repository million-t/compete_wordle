# Generated by Django 5.1.2 on 2024-11-05 08:02

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('contest_type', models.CharField(choices=[('DAILY', 'Daily'), ('CONTEST', 'Contest')], default='CONTEST', max_length=10)),
                ('contest_availability', models.CharField(choices=[('PRIVATE', 'Private'), ('PUBLIC', 'Public')], default='PUBLIC', max_length=10)),
                ('description', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='created_contests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContestParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='participants',
            field=models.ManyToManyField(related_name='participated_contests', through='api.ContestParticipant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='InvitationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=uuid.uuid4, max_length=36, unique=True)),
                ('contest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.contest')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=5)),
                ('word_position', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('weight', models.IntegerField(default=1)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contest')),
            ],
        ),
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_position', models.CharField(max_length=2)),
                ('guess_text', models.CharField(max_length=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.word')),
            ],
        ),
        migrations.AddIndex(
            model_name='contest',
            index=models.Index(fields=['start_time', 'end_time'], name='api_contest_start_t_848a65_idx'),
        ),
    ]
