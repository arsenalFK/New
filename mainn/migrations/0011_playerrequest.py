# Generated by Django 3.0.5 on 2020-05-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0010_auto_20200507_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_request_name', models.CharField(max_length=255)),
                ('player_request_name2', models.CharField(max_length=255)),
                ('player_request_age', models.SmallIntegerField(default=0)),
                ('player_request_contacts', models.TextField(help_text='Контакты (Ном.Тел, Viber, WhatsApp), Skype')),
            ],
        ),
    ]
