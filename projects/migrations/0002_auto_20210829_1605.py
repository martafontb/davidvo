# Generated by Django 3.2.6 on 2021-08-29 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]