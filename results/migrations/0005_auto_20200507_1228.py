# Generated by Django 3.0.6 on 2020-05-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_auto_20200507_1224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'UCI-category', 'verbose_name_plural': 'UCI-Categorieën'},
        ),
        migrations.AlterField(
            model_name='ploegleider',
            name='birthday',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='ploegleider',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='ploegleider',
            name='nickname',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='race',
            name='enddate',
            field=models.DateField(blank=True),
        ),
    ]
