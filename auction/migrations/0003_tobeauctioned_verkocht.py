# Generated by Django 3.0.7 on 2021-01-23 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20210123_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='tobeauctioned',
            name='verkocht',
            field=models.BooleanField(default=False),
        ),
    ]