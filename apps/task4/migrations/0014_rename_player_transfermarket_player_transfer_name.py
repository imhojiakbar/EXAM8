# Generated by Django 5.0.3 on 2024-03-31 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4', '0013_rename_player_name_transfermarket_player'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfermarket',
            old_name='player',
            new_name='player_transfer_name',
        ),
    ]
