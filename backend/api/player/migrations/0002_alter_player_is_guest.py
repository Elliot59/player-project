# Generated by Django 4.1.1 on 2022-09-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='is_guest',
            field=models.BooleanField(default=False),
        ),
    ]
