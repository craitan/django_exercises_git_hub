# Generated by Django 3.2.16 on 2022-10-27 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('category', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Puzzle', 'Puzzle'), ('Strategy', 'Strategy'), ('Sports', 'Sports'), ('Board/Card Game', 'Board/Card Game'), ('Other', 'Other')], max_length=15)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(5.0)])),
                ('image_url', models.URLField()),
                ('max_level', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
