# Generated by Django 3.0.6 on 2020-06-29 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0027_listing_is_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='Make',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='listing_brand',
            new_name='listing_make',
        ),
    ]
