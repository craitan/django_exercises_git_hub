# Generated by Django 3.2.16 on 2022-10-26 14:48

import django.core.validators
from django.db import migrations, models
import music_app_django.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_create_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'), ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30)),
                ('image_url', models.ImageField(upload_to='')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), music_app_django.web.validators.alphanumeric_validator]),
        ),
    ]
