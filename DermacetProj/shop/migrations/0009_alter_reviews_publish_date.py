# Generated by Django 4.1.6 on 2023-05-20 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 20, 18, 44, 17, 680464)),
        ),
    ]