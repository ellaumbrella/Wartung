# Generated by Django 2.1.4 on 2018-12-18 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wartung', '0016_remove_wartungen_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='wartungen',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
