# Generated by Django 3.0 on 2021-02-15 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20210212_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allproduct',
            name='imageurl',
        ),
    ]