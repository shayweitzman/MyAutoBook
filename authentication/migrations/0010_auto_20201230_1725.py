# Generated by Django 3.1.3 on 2020-12-30 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20201228_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adult',
            old_name='taz',
            new_name='ID_Number',
        ),
    ]
