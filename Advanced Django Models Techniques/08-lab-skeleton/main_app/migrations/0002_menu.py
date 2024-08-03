# Generated by Django 5.0.4 on 2024-07-15 13:25

import django.db.models.deletion
import main_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(validators=[main_app.validators.ValidateMenuCategories('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')])),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.restaurant')),
            ],
        ),
    ]
