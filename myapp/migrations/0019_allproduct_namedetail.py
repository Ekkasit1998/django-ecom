# Generated by Django 3.0 on 2021-03-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20210221_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='allproduct',
            name='namedetail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
