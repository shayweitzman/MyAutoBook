# Generated by Django 3.1.3 on 2021-01-04 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_catalog', '0021_auto_20210103_2220'),
        ('authentication', '0021_auto_20201230_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True, default=None, max_length=200, null=True)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book_catalog.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.adult')),
            ],
        ),
    ]
