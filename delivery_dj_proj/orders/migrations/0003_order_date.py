# Generated by Django 3.1.7 on 2021-03-22 06:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_is_recieved'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]