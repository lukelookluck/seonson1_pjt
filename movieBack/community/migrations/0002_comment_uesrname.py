# Generated by Django 2.1.15 on 2020-06-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='uesrname',
            field=models.TextField(default='메롱'),
        ),
    ]
