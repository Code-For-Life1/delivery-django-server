# Generated by Django 3.1.7 on 2021-04-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_driver_is_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unauthdriver',
            name='token',
            field=models.CharField(default='VI46XU', editable=False, max_length=6, primary_key=True, serialize=False),
        ),
    ]
