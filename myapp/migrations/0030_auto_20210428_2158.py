# Generated by Django 3.0 on 2021-04-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_auto_20210428_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpending',
            name='silptime',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
