# Generated by Django 2.0.7 on 2018-11-19 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wartung', '0002_auto_20181029_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endzeit',
            name='wartungen2',
        ),
        migrations.RemoveField(
            model_name='startzeit',
            name='wartungen1',
        ),
        migrations.AddField(
            model_name='wartungen',
            name='endzeit',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='%d/%m/%y %H:%M'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wartungen',
            name='startzeit',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='%d/%m/%y %H:%M'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Endzeit',
        ),
        migrations.DeleteModel(
            name='Startzeit',
        ),
    ]
