# Generated by Django 3.2.7 on 2021-10-12 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0017_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='medewerkers',
        ),
    ]
