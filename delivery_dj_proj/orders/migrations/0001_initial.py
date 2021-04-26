# Generated by Django 3.1.7 on 2021-04-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=80)),
                ('building', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=3)),
                ('receiver_full_name', models.CharField(max_length=60)),
                ('receiver_phone_number', models.CharField(max_length=20)),
                ('is_done', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]
