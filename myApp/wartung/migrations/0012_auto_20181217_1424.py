# Generated by Django 2.0.7 on 2018-12-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wartung', '0011_wartungen_wartungen_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wartungen',
            name='wartungen_name',
            field=models.CharField(max_length=50, verbose_name='Wartungsname'),
        ),
    ]
