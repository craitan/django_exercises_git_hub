# Generated by Django 3.2.16 on 2022-10-30 08:01

import django.core.validators
from django.db import migrations, models
import mid_exam.car_app.validators


class Migration(migrations.Migration):
    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username',
                 models.CharField(max_length=10, validators=[mid_exam.car_app.validators.min_chars_validator])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_picture', models.URLField()),
            ],
        ),
    ]