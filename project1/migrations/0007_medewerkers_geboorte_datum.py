# Generated by Django 3.2.7 on 2021-09-08 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0006_medewerkers_bnsnummer'),
    ]

    operations = [
        migrations.AddField(
            model_name='medewerkers',
            name='geboorte_datum',
            field=models.DateField(null=True),
        ),
    ]
