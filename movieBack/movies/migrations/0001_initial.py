# Generated by Django 2.1.15 on 2020-06-13 10:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('popularity', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('adult', models.BooleanField()),
                ('overview', models.TextField(blank=True)),
                ('original_language', models.CharField(max_length=10)),
                ('poster_path', models.CharField(max_length=100)),
                ('backdrop_path', models.CharField(default='', max_length=100)),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('like', models.ManyToManyField(related_name='like_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
