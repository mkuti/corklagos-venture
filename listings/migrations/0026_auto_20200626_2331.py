# Generated by Django 3.0.6 on 2020-06-26 23:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0025_auto_20200626_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(20.0)]),
        ),
    ]