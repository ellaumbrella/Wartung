# Generated by Django 2.0.7 on 2018-11-26 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wartung', '0008_auto_20181126_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wartungen',
            name='pub_date_modified',
        ),
    ]
