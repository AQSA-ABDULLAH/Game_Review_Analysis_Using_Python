# Generated by Django 4.2.5 on 2023-10-07 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_games_delete_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Games',
            new_name='Game',
        ),
    ]