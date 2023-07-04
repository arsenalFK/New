# Generated by Django 3.0.5 on 2020-05-01 20:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0006_auto_20200501_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_likes',
            field=models.IntegerField(default='0', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
