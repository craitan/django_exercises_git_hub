# Generated by Django 3.2.16 on 2022-10-30 08:22

import django.core.validators
from django.db import migrations, models
import mid_exam.car_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0002_create_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('Sports Car', 'Sports Car'), ('Pickup', 'Pickup'), ('Crossover', 'Crossover'), ('Minibus', 'Minibus'), ('Other', 'Other')], max_length=10)),
                ('car_model', models.CharField(max_length=20, validators=[mid_exam.car_app.validators.min_chars_validator])),
                ('car_year', models.IntegerField(validators=[mid_exam.car_app.validators.validate_year])),
                ('car_image', models.URLField()),
                ('car_price', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
