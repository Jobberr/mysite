# Generated by Django 3.2.7 on 2021-10-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0024_alter_opmerkingen_datum_opmerkingen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opmerkingen',
            name='datum_opmerkingen',
            field=models.DateField(null=True),
        ),
    ]
