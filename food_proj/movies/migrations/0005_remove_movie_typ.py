# Generated by Django 5.0.3 on 2024-04-02 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_typ'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='typ',
        ),
    ]