# Generated by Django 3.0.6 on 2020-06-11 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200607_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('dismantler', 'Irish dismantler'), ('dealer', 'Car dealer')], default='', max_length=15),
        ),
    ]
