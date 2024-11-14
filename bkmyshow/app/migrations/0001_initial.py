# Generated by Django 5.1.2 on 2024-11-14 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date', models.DateField()),
                ('bckgrnd_img', models.FileField(upload_to='')),
                ('lang', models.TextField()),
                ('durtn', models.TextField()),
                ('diamtn', models.TextField()),
                ('type', models.TextField()),
                ('cert', models.TextField()),
                ('about', models.TextField()),
            ],
        ),
    ]
