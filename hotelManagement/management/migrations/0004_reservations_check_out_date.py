# Generated by Django 3.2.8 on 2022-01-15 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20220114_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='check_out_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
