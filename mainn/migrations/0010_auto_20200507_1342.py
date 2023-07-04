# Generated by Django 3.0.5 on 2020-05-07 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0009_auto_20200506_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_position',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Вратарь'), (2, 'Защитник'), (3, 'Полузащитник'), (6, 'Полунападающий'), (4, 'Нападающий'), (5, 'На замене')], default=5, help_text='Позиция'),
        ),
    ]
