# Generated by Django 5.0 on 2023-12-17 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0002_watchlist_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='platform',
            new_name='stream',
        ),
    ]
