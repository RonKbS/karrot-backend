# Generated by Django 2.2.7 on 2019-11-20 21:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0040_auto_20190914_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='features',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None),
        ),
    ]
