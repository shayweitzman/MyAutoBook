# Generated by Django 3.1.3 on 2020-11-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0007_auto_20201130_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='book_catalog/images/defult.png', upload_to='book_catalog/images'),
        ),
    ]