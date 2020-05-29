# Generated by Django 3.0.6 on 2020-05-28 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0021_auto_20200528_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='results.Country', to_field='alpha3'),
        ),
    ]
