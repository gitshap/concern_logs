# Generated by Django 3.2.7 on 2021-09-29 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concerns', '0006_alter_concerns_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='concerns',
            name='additional_notes',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]