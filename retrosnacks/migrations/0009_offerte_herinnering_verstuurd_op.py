# Generated by Django 5.1.6 on 2025-05-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retrosnacks', '0008_klant'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerte',
            name='herinnering_verstuurd_op',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Datum herinnering verstuurd'),
        ),
    ]
