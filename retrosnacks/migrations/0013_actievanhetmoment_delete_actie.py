# Generated by Django 5.1.6 on 2025-05-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retrosnacks', '0012_actie_delete_actievanhetmoment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActieVanHetMoment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('omschrijving', models.TextField()),
                ('actief_tot', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Actie',
        ),
    ]
