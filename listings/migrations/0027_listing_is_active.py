# Generated by Django 3.0.6 on 2020-06-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0026_auto_20200626_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
