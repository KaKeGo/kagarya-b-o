# Generated by Django 4.2.2 on 2023-08-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangalist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mangalist',
            name='orginal_slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]