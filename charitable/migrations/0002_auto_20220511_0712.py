# Generated by Django 3.2.9 on 2022-05-11 07:12

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='don',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='images'),
        ),
        migrations.AddField(
            model_name='nongo',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='images'),
        ),
    ]
