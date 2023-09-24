# Generated by Django 4.2.2 on 2023-09-24 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mangalist', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='raiting',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manga_ratings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mangalist',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mangalist',
            name='category',
            field=models.ManyToManyField(to='mangalist.category'),
        ),
        migrations.AddField(
            model_name='mangalist',
            name='manga_type',
            field=models.ManyToManyField(to='mangalist.type'),
        ),
        migrations.AlterUniqueTogether(
            name='raiting',
            unique_together={('manga', 'user')},
        ),
    ]