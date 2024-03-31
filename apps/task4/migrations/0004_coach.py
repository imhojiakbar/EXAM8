# Generated by Django 5.0.3 on 2024-03-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task4', '0003_delete_coach'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('nationality', models.CharField(max_length=100)),
                ('experience_years', models.PositiveIntegerField()),
                ('number_of_managed_clubs', models.PositiveIntegerField()),
                ('number_of_titles_won', models.PositiveIntegerField()),
            ],
        ),
    ]
