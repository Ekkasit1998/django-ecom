# Generated by Django 3.0 on 2021-01-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='stemp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
