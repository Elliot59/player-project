# Generated by Django 4.1.1 on 2022-09-14 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_alter_player_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='confirm_password',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
