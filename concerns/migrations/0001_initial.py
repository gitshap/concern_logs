# Generated by Django 3.2.7 on 2021-09-27 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concerns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=255)),
                ('findings', models.CharField(max_length=255)),
                ('resolution', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
