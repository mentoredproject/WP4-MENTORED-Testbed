# Generated by Django 4.0.5 on 2022-06-20 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippet',
            new_name='Experiment',
        ),
    ]
