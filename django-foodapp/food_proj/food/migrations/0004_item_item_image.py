# Generated by Django 5.0.3 on 2024-03-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://lh3.googleusercontent.com/RLo2nYsnoSNTVTCZoiRslZwFtt3FFCFZZG1wVPTAVgZ60P5thfiEWMuGesDHqOff983Z=w170', max_length=500),
        ),
    ]
