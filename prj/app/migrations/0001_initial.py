# Generated by Django 5.1.3 on 2024-11-05 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.TextField()),
                ('name', models.TextField()),
                ('p_type', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.FileField(upload_to='')),
                ('stock', models.IntegerField()),
                ('disp', models.TextField()),
            ],
        ),
    ]
