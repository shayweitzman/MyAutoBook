# Generated by Django 3.1.3 on 2021-01-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0018_auto_20210103_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Damage_Description',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
