# Generated by Django 3.0.5 on 2020-04-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.URLField(unique=True),
        ),
    ]
