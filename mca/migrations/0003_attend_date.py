# Generated by Django 3.0.1 on 2020-03-31 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mca', '0002_attend'),
    ]

    operations = [
        migrations.AddField(
            model_name='attend',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
