# Generated by Django 3.1.1 on 2020-12-21 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('duration', models.FloatField()),
                ('genre', models.CharField(max_length=30)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_track', to='app.album')),
            ],
            options={
                'ordering': ['genre'],
                'unique_together': {('album', 'title')},
            },
        ),
    ]
