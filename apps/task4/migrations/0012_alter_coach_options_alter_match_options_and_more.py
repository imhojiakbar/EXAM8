# Generated by Django 5.0.3 on 2024-03-31 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task4', '0011_title_remove_coach_number_of_titles_won_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name': 'Coaches', 'verbose_name_plural': 'Coaches'},
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': 'Matches', 'verbose_name_plural': 'Matches'},
        ),
        migrations.AddField(
            model_name='team',
            name='championship',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='championship_name', to='task4.championship'),
            preserve_default=False,
        ),
    ]
