# Generated by Django 3.2.7 on 2021-09-29 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concerns', '0002_auto_20210927_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concerns',
            old_name='findings',
            new_name='problems',
        ),
    ]
