# Generated by Django 5.1.2 on 2024-11-01 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_id',
            field=models.Field(),
        ),
    ]
