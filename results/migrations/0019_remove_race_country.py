# Generated by Django 3.0.6 on 2020-05-08 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0018_auto_20200508_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='country',
        ),
    ]
