# Generated by Django 4.2.2 on 2023-08-21 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameslist', '0003_alter_rating_user_usergamelist_games_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='game_list',
            field=models.ManyToManyField(blank=True, to='gameslist.usergamelist'),
        ),
    ]
