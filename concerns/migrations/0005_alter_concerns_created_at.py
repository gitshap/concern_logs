# Generated by Django 3.2.7 on 2021-09-29 03:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('concerns', '0004_rename_problems_concerns_problem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concerns',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
