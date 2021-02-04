# Generated by Django 3.1.3 on 2021-01-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='book_catalog/images')),
                ('date', models.DateField()),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]