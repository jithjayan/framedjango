# Generated by Django 5.1.2 on 2024-11-20 03:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='ot_lang',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]