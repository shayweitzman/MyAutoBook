# Generated by Django 3.1.3 on 2021-01-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20210103_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(default='home/images/defult2.jpg', upload_to='home/images'),
        ),
    ]
