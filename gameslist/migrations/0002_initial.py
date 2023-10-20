# Generated by Django 4.2.2 on 2023-10-20 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gameslist', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usergameentry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='platform',
            name='creator',
            field=models.ManyToManyField(blank=True, to='gameslist.platformcreator'),
        ),
        migrations.AddField(
            model_name='gamelist',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gamelist',
            name='category',
            field=models.ManyToManyField(blank=True, to='gameslist.category'),
        ),
        migrations.AddField(
            model_name='gamelist',
            name='comments',
            field=models.ManyToManyField(blank=True, to='gameslist.comment'),
        ),
        migrations.AddField(
            model_name='gamelist',
            name='developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game_developer', to='gameslist.gamedeveloper'),
        ),
        migrations.AddField(
            model_name='gamelist',
            name='game_type',
            field=models.ManyToManyField(blank=True, to='gameslist.type'),
        ),
        migrations.AddField(
            model_name='gamelist',
            name='platforms',
            field=models.ManyToManyField(blank=True, to='gameslist.platform'),
        ),
        migrations.AddField(
            model_name='gamelist',
            name='tags',
            field=models.ManyToManyField(blank=True, to='gameslist.tag'),
        ),
        migrations.AddField(
            model_name='gamedeveloper',
            name='founders',
            field=models.ManyToManyField(blank=True, to='gameslist.founder'),
        ),
        migrations.AddField(
            model_name='commentraiting',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gameslist.comment'),
        ),
        migrations.AddField(
            model_name='commentraiting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gameslist.gamelist'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gamelist',
            name='game_publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game_publisher', to='gameslist.gamepublisher'),
        ),
        migrations.AlterUniqueTogether(
            name='commentraiting',
            unique_together={('user', 'comment', 'comment_rating')},
        ),
    ]
