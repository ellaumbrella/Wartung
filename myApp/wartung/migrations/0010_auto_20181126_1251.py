# Generated by Django 2.0.7 on 2018-11-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wartung', '0009_remove_wartungen_pub_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wartungen',
            name='wartungen_text',
            field=models.TextField(max_length=200, verbose_name='Wartungstext'),
        ),
    ]
