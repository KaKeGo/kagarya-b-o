# Generated by Django 4.2.2 on 2023-06-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('access', models.CharField(choices=[('admin', 'Admin'), ('authenticated', 'Authenticated User'), ('any', 'Any')], default='admin', max_length=20)),
                ('url', models.CharField(max_length=255)),
                ('url_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ApiCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('api', models.ManyToManyField(blank=True, null=True, to='home.apiurls')),
            ],
        ),
    ]
