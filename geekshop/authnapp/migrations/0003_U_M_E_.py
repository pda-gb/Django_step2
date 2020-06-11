# Generated by Django 2.2.3 on 2020-06-11 08:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0002_create_debug_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='ключ подтверждения'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 13, 8, 38, 22, 218352, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
