# Generated by Django 3.0 on 2021-04-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_auto_20210428_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpending',
            name='silptime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
